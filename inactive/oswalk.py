import os

# Set the directory you want to start from
rootDir = './image'

# Initialize an empty list to store the file names
file_names = []

# Use os.walk to iterate through all the subdirectories in the root directory
for dirName, subdirList, fileList in os.walk(rootDir):
    # Iterate through all the files in the current subdirectory
    for fname in fileList:
        # If the file is a JPG file, add it to the list
        if fname.endswith('.jpg'):
            file_names.append(fname)

# Print the list of file names
print(file_names)