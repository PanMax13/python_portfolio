# this script will change photo

from PIL import Image
import subprocess
import os, subprocess

directory = '.'

for filename in os.listdir(directory): #check all files in derictory on unreadble for our library.
    if filename.lower().endswith(".heic"): #if photo's format is heic, converting it to jpeg
        print('Converting %s...' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % filename, "%s" % (filename[0:-5] + '.jpg')])


photo = input("Type the name of photo: ") # get name of photo




def crop( x1, y1, x2, y2, image): # this function is cropping image
    image = Image.open(image).crop((x1, y1, x2, y2)) #cropping image
    image.save("./cropped.jpg") #saving
    delete = input('Do u want to delete original? y/n ') # askin an user, delete or not the original image
    if delete == 'y':
        os.remove(image)
    image.show() # showing the picture


def change_contrast(image):
    color = input("On which color you need to change img?(black(1), gray(L)): ") # asking the user how contrast to set on image
    image = Image.open(image).convert(f"{color}", dither=Image.NONE) # convert the image to choosed by user color
    image.save("color changed.jpg") # saving photo
    delete = input('Do u want to delete original? y/n ') # askin an user, delete or not the original image
    if delete == 'y':
        os.remove(image)
    image.show()


while all != "y": # if user need to change all in photo, create a loop, which will work until the user stop it
    what_to_do = input("What do you want to change?(cropping(crop), change contrast(cc)):  ") # asking the user to what to do
    if all == "y": # check user's answer from 55th string
        break
    else:
        if what_to_do == "crop": # check on call crop-function
            x1 = int(input("First dot x1: ")) # asking x,y dots to cut image
            y1 = int(input("First dot y1: "))
            x2 = int(input("Second dot x2: "))
            y2 = int(input("Second dot y2: "))
            crop(x1, y1, x2, y2, f"./{photo}") # call the function
        elif what_to_do == "cc": # check on call change contrast function
            change_contrast(f"./{photo}") # call the funciton
        all = input("That's all? y/n: ") # asking the user is he end or not.
