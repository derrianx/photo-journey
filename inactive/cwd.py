import os
import csv

# Get a list of all files in the current directory
files = os.listdir()

# Open a CSV file for writing
with open('file_names.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  
  # Write the file names to the CSV file
  for file in files:
    writer.writerow([file])
