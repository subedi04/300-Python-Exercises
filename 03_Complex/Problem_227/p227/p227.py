'''
Write a Python Program to display image using openv 
'''

import cv2

if __name__=="__main__":
    img = cv2.imread("image.png")
    cv2.imshow("Image Title", img)
    cv2.waitKey(0)

