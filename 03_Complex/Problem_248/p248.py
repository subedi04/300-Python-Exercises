'''
Write a Python Program to write text on picture
'''
from PIL import Image, ImageDraw

img = Image.open("image.png")
text = "How are you"
draw_img = ImageDraw.Draw(img)
draw_img.text((10,50), text, (234,24,54))
# img.save()
img.show()