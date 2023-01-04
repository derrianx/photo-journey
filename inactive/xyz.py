import exifread
import os
import csv

# Specify the directory containing the image files
cwd = os.getcwd()
file_path = os.path.join(cwd, 'xyz.py')
directory = file_path

# Open the CSV file for writing
with open('metadata.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Filename', 'ISO', 'Aperture', 'Shutter Speed', 'Focal Length'])

    # Iterate through all the files in the directory
    for filename in os.listdir(directory):
        # Only process JPEG files
        if filename.endswith('.jpg'):
            # Open the image file
            with open(os.path.join(directory, filename), 'rb') as f:
                # Extract EXIF metadata
                tags = exifread.process_file(f)

            # Write the metadata for the current image to the CSV file
            writer.writerow([filename, tags["EXIF ISOSpeedRatings"], tags["EXIF FNumber"], tags["EXIF ExposureTime"], tags["EXIF FocalLength"]])
