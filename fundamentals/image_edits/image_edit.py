#PIL or Pillow is a python module for image maniplation. Use case: for handling manipulation of pictures like "passport photo" or generating image from an existing picture
from PIL import Image #PIL was automatically imported with the pillow package (Pillow is the updated form of PIL)

dog_image = Image.open("./pics/dog_pic.jpg")

dog_image.show() #for displaying the file

# GETTING IMAGE INFORMATION 
print(dog_image.format) #this outputs the file format e.g. png of jpg
print(dog_image.mode) #this outputs the colour mode e.g. RGB or CMYK or more
print(dog_image.size) #this outputs the pixel dimension

# IMAGE MANIPULATION
# 1. Convert to Black and White
black_n_white_ver = dog_image.convert("L") #this extracts only the luminance of the image without the colors so making it black and white
black_n_white_ver.show()

# 2. reduce the size
small_dig_pic = dog_image.resize((125,125))
small_dig_pic.show()

# 3. rotate image
rotated_image = dog_image.rotate(45) #rotate 45 degrees
rotated_image.show()

# 4. save as new format
small_dig_pic.save("./pics/dog_pic_small.png") #save with PNG extension

# 5. save thumbnail
import glob, os

thumnail_size = (128, 90)

for infile in glob.glob("./pics/*.jpg"): #get the list of file paths matching the provided pattern
    new_dog_img = Image.open(infile)

    #getting the file name so we can keep the name for the thumbnail
    path, filename_n_ext = os.path.split(infile) #split the current full file path into path and file name + extension
    filename = filename_n_ext.split(".")[0] #get the file name
    
    #convert image 2 thumbnail
    new_dog_img.thumbnail(thumnail_size) #(NOTE: this modifies in-place) this function changes the image into thumbnail size while preserving the aspect of the image
    new_dog_img.save(f"{path}/exported_thumbnails/{filename}.thumbnail", "JPEG") #save with thumbnail extension using jpeg format


