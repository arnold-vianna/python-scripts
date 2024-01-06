import subprocess

def update_github_repo(commit_message):
    """Stages, commits, and pushes changes to a GitHub repository."""

    try:
        subprocess.run(["sudo", "git", "add", "."], check=True)
        subprocess.run(["sudo", "git", "status"], check=True)
        subprocess.run(["sudo", "git", "commit", "-am", commit_message], check=True)
        subprocess.run(["sudo", "git", "push", "origin", "main"], check=True)
        print("Changes pushed to GitHub successfully!")
    except subprocess.CalledProcessError as error:
        print("Error occurred:", error)

# Example usage:
commit_message = "Updated files"  # Replace with your desired commit message
update_github_repo(commit_message)
