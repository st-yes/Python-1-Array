import numpy as np
from PIL import Image

image_address = "landscape.jpg"
def ft_load(path: str):
    try:
        image_object = Image.open(image_address)
        image_array = np.asarray(image_object)
        print("The shape of image is: ", image_array.shape)
        return (image_array)
    except:
        print("error in inputted image")


# def ft_load(path: str): #(you can return to the desired format)
