'''
Write a Python Program to Blur an image
'''

import cv2

if __name__=="__main__":
    img = cv2.imread("image.png")
    blur_Image = cv2.blur(img,(100,10))
    cv2.imshow("Title of real image", img)
    cv2.imshow("Title image", blur_Image)
    cv2.waitKey(0)
