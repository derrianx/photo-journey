#this version prints only a specific image file 

import csv
import exifread
from PIL import Image


# Open the file in binary mode
with open('image/DSC00663.jpg', 'rb') as f:
    # Extract the EXIF metadata from the file
    exif_data = exifread.process_file(f)

# Open the CSV file in write mode
with open('exif_data.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Tag', 'Value'])

    # Loop through the EXIF data
    for tag, value in exif_data.items():
        # Write the tag and value to the CSV file
        writer.writerow([tag, value])
