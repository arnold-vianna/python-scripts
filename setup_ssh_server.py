import os

def install_ssh_server():
    os.system("sudo apt-get update")  # Update the package list
    os.system("sudo apt-get install -y openssh-server")  # Install OpenSSH server

def start_ssh_server():
    os.system("sudo systemctl start ssh")  # Start the SSH server

def enable_ssh_server():
    os.system("sudo systemctl enable ssh")  # Enable the SSH server to start on boot

def status_ssh_server():
    os.system("sudo systemctl status ssh")  # Check the status of the SSH server

if __name__ == "__main__":
    install_ssh_server()
    start_ssh_server()
    enable_ssh_server()
    status_ssh_server()
