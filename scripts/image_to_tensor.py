from keras.preprocessing import image
from PIL import Image

def image_to_tensor(img):
    file = image.load_img(file,target_size=(224,224))
    # standardize pixel values based on 255 possible RGB values
    arr = image.img_to_array(img) * (1.0/255.0)
    return arr