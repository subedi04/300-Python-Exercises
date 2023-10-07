'''
Write a Python Program to join two pictures.
'''

import cv2

# Read the images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Create a new image that is the size of both images
new_img = cv2.hconcat([img1, img2])

# Save the new image
cv2.imwrite('new_image.jpg', new_img)
