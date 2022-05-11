import PIL
from PIL import Image, ImageTk


def background(img_path, resolution: tuple):
    bg1 = Image.open(img_path).rotate(90, PIL.Image.NEAREST, expand=True)
    bg1 = bg1.resize(resolution, Image.ANTIALIAS)
    return bg1


def button(img_path, width, height):
    btn = Image.open(img_path)
    btn = btn.resize((width, height), Image.ANTIALIAS)
    return btn
