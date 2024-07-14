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


import os
import datetime

def file_date(filename):
    # Check if the filename is a directory, change the filename if it is
    if os.path.isdir(filename):
        filename = "new_file.txt"  # Change to a new filename

    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass  # Just creating the file, no need to write anything
    
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.date.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{:%Y-%m-%d}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return os.path.os.path.abspath(relative_parent)

print(parent_directory())