##  A simple multi archive management tool.
##  Ensure you have the necessary libraries installed
##  pip install rarfile py7zr
##  https://github.com/arnold-vianna


import zipfile
import tarfile
import shutil
import rarfile  # Ensure you have installed it with `pip install rarfile`
import os

archive_types = {
    "ZIP": "ZIP (.zip): Widely used due to its support across various operating systems and applications.",
    "RAR": "RAR (.rar): Known for its high compression ratios and the ability to split archives into parts.",
    "7z": "7z (.7z): Offers strong compression and encryption capabilities.",
    "TAR": "TAR (.tar): Commonly used on Unix and Linux systems, often combined with compression methods like Gzip.",
    "Gzip": "Gzip (.gz): Frequently used in combination with TAR files (e.g., .tar.gz) for compression on Unix and Linux systems.",
    "Bzip2": "Bzip2 (.bz2): Another compression method often used with TAR files (e.g., .tar.bz2) for better compression ratios than Gzip.",
    "XZ": "XZ (.xz): Provides high compression ratios and is often used with TAR files (e.g., .tar.xz).",
    "ISO": "ISO (.iso): Represents a disk image of an optical disc, such as a CD or DVD.",
    "CAB": "CAB (.cab): Used by Microsoft for software installation packages.",
    "LZH": "LZH (.lzh): Popular in Japan, known for its use in older software and archives.",
    "ARJ": "ARJ (.arj): Used primarily in the DOS era for file compression and archiving.",
    "ACE": "ACE (.ace): Known for its high compression rates but less commonly used now due to proprietary issues.",
    "LZMA": "LZMA (.lzma): A high compression ratio algorithm used in 7z and other archives.",
    "Z": "Z (.Z): A Unix compression format that is mostly obsolete, replaced by Gzip and Bzip2.",
    "DMG": "DMG (.dmg): A disk image format used by macOS to distribute software."
}

def show_menu():
    print("\nMenu:")
    print("1. Archive a file or directory")
    print("2. Open an archive")
    print("3. See archive format descriptions")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def show_format_descriptions():
    print("\nArchive Format Descriptions:")
    for format, description in archive_types.items():
        print(f"{description}")

def archive_file():
    file_path = input("Enter the full path of the file or directory to archive: ")
    print("\nAvailable archive formats:")
    for idx, format in enumerate(archive_types.keys(), 1):
        print(f"{idx}. {format}")
    format_choice = int(input("Choose an archive format (number): "))
    chosen_format = list(archive_types.keys())[format_choice - 1]
    output_path = input("Enter the output archive path (with extension): ")

    if chosen_format == "ZIP":
        with zipfile.ZipFile(output_path, 'w') as zipf:
            if os.path.isdir(file_path):
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        zipf.write(os.path.join(root, file))
            else:
                zipf.write(file_path)
    elif chosen_format == "RAR":
        with rarfile.RarFile(output_path, 'w') as rarf:
            rarf.write(file_path)
    elif chosen_format == "7z":
        with py7zr.SevenZipFile(output_path, 'w') as sevenz:
            sevenz.writeall(file_path)
    elif chosen_format == "TAR":
        with tarfile.open(output_path, 'w') as tar:
            tar.add(file_path)
    elif chosen_format == "Gzip":
        with tarfile.open(output_path, 'w:gz') as tar:
            tar.add(file_path)
    elif chosen_format == "Bzip2":
        with tarfile.open(output_path, 'w:bz2') as tar:
            tar.add(file_path)
    elif chosen_format == "XZ":
        with tarfile.open(output_path, 'w:xz') as tar:
            tar.add(file_path)
    else:
        print(f"{chosen_format} format is not yet supported in this script.")
    
    print(f"File archived as {output_path}")

def open_archive():
    archive_path = input("Enter the full path of the archive to open: ")
    output_dir = input("Enter the directory where to extract the archive: ")

    if archive_path.endswith(".zip"):
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(output_dir)
    elif archive_path.endswith(".rar"):
        with rarfile.RarFile(archive_path, 'r') as rarf:
            rarf.extractall(output_dir)
    elif archive_path.endswith(".7z"):
        with py7zr.SevenZipFile(archive_path, 'r') as sevenz:
            sevenz.extractall(output_dir)
    elif archive_path.endswith((".tar", ".tar.gz", ".tar.bz2", ".tar.xz")):
        with tarfile.open(archive_path, 'r') as tar:
            tar.extractall(output_dir)
    else:
        print(f"{archive_path} format is not yet supported in this script.")
    
    print(f"Archive extracted to {output_dir}")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            archive_file()
        elif choice == "2":
            open_archive()
        elif choice == "3":
            show_format_descriptions()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
