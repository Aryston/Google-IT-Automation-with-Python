import os

def create_python_script(filename):
    """
    Creates a Python script with a standard header comment and returns its size.

    Args:
        filename (str): The name of the file to create.

    Returns:
        int: The size of the created file in bytes.
    """
    comments = "# Start of a new Python program"  # Initial comment for the file

    with open(filename, "w") as f:
        f.write(comments)  # Write the comment to the file

    filesize = os.path.getsize(filename)  # Get file size after writing comment
    return filesize


# Example usage
print(create_python_script("program.py"))
