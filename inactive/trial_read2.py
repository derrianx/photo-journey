import os
import exifread
import csv

# get a list of all the JPEG files in the 'image' folder
jpg_files = [f for f in os.listdir('image') if f.endswith('.jpg')]

# open a CSV file for writing
with open('habit_data.csv', 'w', newline='') as csvfile:
  fieldnames = ['filename', 'iso_speed', 'shutter_speed_value', 'max_aperture_value', 'focal_length']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # write the header row
  writer.writeheader()

  # loop through the JPEG files
  for jpg_file in jpg_files:
    # open the JPEG file
    with open(os.path.join('image', jpg_file), 'rb') as f:
      # read the EXIF metadata
      tags = exifread.process_file(f)

    # extract the 'iso_speed', 'shutter_speed_value', 'max_aperture_value', and 'focal_length' data
    iso_speed = tags.get('EXIF ISOSpeedRatings')
    shutter_speed_value = tags.get('EXIF ShutterSpeedValue')
    max_aperture_value = tags.get('EXIF MaxApertureValue')
    focal_length = tags.get('EXIF FocalLength')

    # write the data to the CSV file
    writer.writerow({'filename': jpg_file, 'iso_speed': iso_speed, 'shutter_speed_value': shutter_speed_value, 'max_aperture_value': max_aperture_value, 'focal_length': focal_length})
