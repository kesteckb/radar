from PIL import Image

im = Image.open("images/object_detect.png")
print(im.format, im.size, im.mode)
im.show()