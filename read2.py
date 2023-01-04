import os
import exifread
from PIL import Image
import csv

# set the folder path
folder_path = 'images'

# open the JPEG file
with open('image/DSC00751.jpg', 'rb') as f:
  # read the EXIF metadata
  tags = exifread.process_file(f)

# extract the 'iso_speed', 'shutter_speed_value', 'max_aperture_value', and 'focal_length' data
iso_speed = tags.get('EXIF ISOSpeedRatings')
shutter_speed_value = tags.get('EXIF ShutterSpeedValue')
max_aperture_value = tags.get('EXIF MaxApertureValue')
focal_length = tags.get('EXIF FocalLength')

# open a CSV file for writing
with open('koi_data.csv', 'w', newline='') as csvfile:
  fieldnames = ['iso_speed', 'shutter_speed_value', 'max_aperture_value', 'focal_length']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # write the header row
  writer.writeheader()

  # write the data to the CSV file
  writer.writerow({'iso_speed': iso_speed, 
  'shutter_speed_value': shutter_speed_value, 
  'max_aperture_value': max_aperture_value, 'focal_length': focal_length})