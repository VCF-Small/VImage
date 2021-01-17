from PIL import Image, ImageEnhance, ImageFilter
from numpy.lib.type_check import imag


def Brightness_Control(image, value):
    factor = float(value/100)
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def Contrast_Control(image, value):
    factor = value/100
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)
        
def Sharpness_Control(image, value):
    factor = float(value/100)
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)

def Saturation_Control(image, value):
    factor = float(value/100)
    return ImageEnhance.Color(image).enhance(factor)
    
def Hue_Control(image, value):
    factor = value
    if(factor == 0):
        pass
    elif(factor > 5):
        pixels = image.load()
        for i in range(image.width):
            for j in range(image.height):
                r,g,b = pixels[i, j]
                g = g + factor/2
                b = b + factor/2
    elif(factor < -5):
        pixels = image.load()
        for i in range(image.width):
            for j in range(image.height):
                r,g,b = pixels[i, j]
                r = r - factor/2   

    return image
        
def Rotate(image, angle):
    return image.rotate(angle)

def Flip(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


