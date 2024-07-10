import os

# Get the current working directory
current_directory = os.getcwd()
print("The current working directory is:", current_directory)

# Print only callable methods from the os module
for attribute in dir(os):
    if callable(getattr(os, attribute)):
        print(attribute)

print(os.environ.get('PATH'))

print("---------------------")

file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
#	print(os.path.isfile(file)) #greska u kodu, duplic
    print("File not found")
print("---------------------")

print(os.getcwd())

print("---------------------")

print(os.listdir("igorsenv1"))

print("---------------------")

dir = "igorsenv1"
for name in os.listdir(dir):
     fullname = os.path.join(dir, name) # odavde kreira full path
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))

print("---------------------")

# Create a directory and move a file from one directory to another
# using low-level OS functions.

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
import os  # Ensure this is included at the top if not already there

dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
try:
    os.rename(src_file, dest_file)
    print("File moved successfully.")
except FileNotFoundError:
    print("Error: The source file does not exist.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")

print("---------------------")