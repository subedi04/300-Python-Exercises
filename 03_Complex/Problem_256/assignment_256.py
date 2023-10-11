'''
Write a Python Program to extract the html from the page. 
Using other than our method.
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
        
        # Print the parsed HTML content
        print(soup.prettify())
    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
