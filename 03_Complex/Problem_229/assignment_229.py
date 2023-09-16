'''
Write a Python Program to find size of an image in MB.
'''

import os

def get_image_size(image_path):
    # Get the size of the image in bytes
    size_in_bytes = os.path.getsize(image_path)

    # Convert bytes to megabytes (1 MB = 1024 * 1024 bytes)
    size_in_mb = size_in_bytes / (1024 * 1024)

    return size_in_mb

if __name__=="__main__":
    image_path = "your_image.jpg"  
    image_size_mb = get_image_size(image_path)

    print(f"The size of the image is approximately {image_size_mb:.2f} MB")
