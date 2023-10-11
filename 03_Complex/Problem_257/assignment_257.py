'''
Write a Python Program to display title of any web page using web scraping. With other method 
'''

import requests
from bs4 import BeautifulSoup


url = 'https://example.com'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and display the title of the web page
        title = soup.title.string
        print(f'Title of the web page: {title}')
    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
