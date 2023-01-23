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



# new idea with dalle

The official DALL-E GitHub repository (https://github.com/lucidrains/DALLE-pytorch) provides a detailed tutorial on how to train DALL-E on a custom dataset. It includes instructions for preparing the dataset, training the model, and generating new images.

The OpenAI website (https://openai.com/dall-e/) also provides a tutorial on how to train DALL-E on a custom dataset, including instructions on how to use the OpenAI API to generate images from text prompts.

There is a tutorial in the Hugging Face website (https://huggingface.co/blog/dall-e-2-image-generation-tutorial) which provides a step-by-step guide on how to train DALL-E on a custom dataset and use it to generate new images.

It is important to note that the training of DALL-E is a computationally intensive task, it may require a powerful GPU and a lot of memory.
