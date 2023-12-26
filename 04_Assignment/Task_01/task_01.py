'''
Build a command-line application that allows users to search 
for and download images from the internet using Python 
libraries such as Requests, BeautifulSoup, and Pillow.
'''
# pip install requests beautifulsoup4 Pillow

import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def search_and_download_images(query, download_path, num_images=5):
    # Create download directory if not exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    search_url = f"https://www.google.com/search?q={query}&tbm=isch"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img', class_='t0fcAb')

    for i, img_tag in enumerate(image_tags[:num_images]):
        img_url = img_tag['src']
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))

        # Save image to the specified directory
        img_path = os.path.join(download_path, f"{query}_{i+1}.jpg")
        img.save(img_path)
        print(f"Image {i+1} downloaded: {img_path}")

if __name__ == "__main__":
    search_query = input("Enter search query: ")
    download_folder = input("Enter download folder (press Enter for current folder): ")

    if not download_folder:
        download_folder = os.getcwd()

    num_images_to_download = int(input("Enter the number of images to download: "))

    search_and_download_images(search_query, download_folder, num_images_to_download)
