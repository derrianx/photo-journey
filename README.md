# photo-journey
documentation of film photography resources 

Credits to chatgpt for generating this idea
A tool for analyzing the exposure settings of your film photographs. This project could involve building a program that extracts metadata from your film photographs (e.g. ISO, aperture, shutter speed) and generates graphs or statistics to help you understand your shooting habits and identify any patterns or trends.


# Initial problem
read.py is not able to read all the files

## Resolution
I went on to download to exiftool and managed to output the entire directory onto a csv file 

That is how i get my data set to begin analysis
documentation: https://exiftool.org/faq.html#Q12
exiftool -csv -r image > out.csv
    1 directories scanned
   95 image files read

# resources
## pandas
https://datatofish.com/convert-string-to-float-dataframe/
https://www.w3schools.com/python/pandas/pandas_plotting.asp


## exif
https://photo.stackexchange.com/
https://buildmedia.readthedocs.org/media/pdf/exif/latest/exif.pdf
### csv file
https://exiftool.org/faq.html#Q12   

