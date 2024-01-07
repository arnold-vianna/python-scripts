#!/usr/bin/env python3

#Author: Arnold Vianna
#https://github.com/arnold-vianna

import subprocess

def update_github_repo(commit_message, branch_name="main"):
    """Stages, commits, and pushes changes to a GitHub repository."""

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-am", commit_message], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)
        print("Changes pushed to GitHub successfully!")
    except subprocess.CalledProcessError as error:
        print(f"An error occurred during Git command: {error}")

# Example usage:
commit_message = "Updated files"
update_github_repo(commit_message)  # Pushes to "main" branch by default

# To push to a different branch:
update_github_repo(commit_message, "feature-branch")
