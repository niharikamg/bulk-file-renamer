import os

def list_files(directory):
    """Lists all files in the given directory."""
    try:
        files = os.listdir(directory)
        print("Files in directory:", files)
    except FileNotFoundError:
        print("Error: Directory not found.")

# Example usage
dir_path = input("Enter directory path: ")
list_files(dir_path)
