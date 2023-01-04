#this version prints only a specific image file 

import csv
import exifread
from PIL import Image

#declar field names first
# fieldnames = ['iso_speed', 'shutter_speed_value', 
#               'max_aperture_value', 'focal_length']
# Open the file in binary mode
with open('image/DSC00663.JPG', 'rb') as f:
    # Extract the EXIF metadata from the file
    exif_data = exifread.process_file(f)

# extract the 'iso_speed', 'shutter_speed_value',
# 'max_aperture_value', and 'focal_length' data
iso_speed = tags.get('EXIF ISOSpeedRatings')
shutter_speed_value = tags.get('EXIF ShutterSpeedValue')
max_aperture_value = tags.get('EXIF MaxApertureValue')
focal_length = tags.get('EXIF FocalLength')

# Open the CSV file in write mode
with open('exif_data.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Tag', 'Value'])

    # Loop through the EXIF data
    for tag, value in exif_data.items():
        # my input test
        # Write the tag and value to the CSV file
        if tag not in ('iso_speed', 'shutter_speed_value', 
        'max_aperture_value', 'focal_length'):
            writer.writerow([tag, value])


# • iso_speed
# • shutter_speed_value
# • max_aperture_value
# • focal_length
