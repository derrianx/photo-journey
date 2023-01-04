import glob

# Get a list of all the .jpg files in the "folder" directory
file_list = glob.glob('image/*.jpg')

# Create an empty buffer
buffer = bytearray()

# Loop through the files
for file_path in file_list:
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the contents of the file into the buffer
        buffer += f.read()


# Open the output file in binary write mode
with open('test.txt', 'wb') as f:
    # Write the contents of the buffer to the file
    f.write(buffer)


# Decode the contents of the buffer as UTF-8 text
text = buffer.decode('utf-8')

# Open the output file in text write mode
with open('lol.txt', 'w') as f:
    # Write the text to the file
    f.write(text)
