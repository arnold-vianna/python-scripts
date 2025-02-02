import hashlib

# this script is made to hash a password using SHA-256 algorithm

# Prompt for the password
password = input("Enter your password: ")

# Hash the password using SHA-256
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Display the resulting hash
print(f"SHA-256 hash: {hashed_password}")
