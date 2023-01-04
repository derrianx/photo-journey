import csv
import exifread
from PIL import Image
# Create a list of file names
filenames = ['image/DSC00663.jpg', 'image/DSC00664.jpg', 'image/DSC00665.jpg']

# Open the CSV file in write mode
with open('no_data.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Filename', 'Tag', 'Value'])

    # Loop through the list of filenames
    for filename in filenames:
        # Open the file in binary mode
        with open(filename, 'rb') as f:
            # Extract the EXIF metadata from the file
            exif_data = exifread.process_file(f)

        # Loop through the EXIF data
        for tag, value in exif_data.items():
            # Write the filename, tag, and value to the CSV file
            writer.writerow([filename, tag, value])
