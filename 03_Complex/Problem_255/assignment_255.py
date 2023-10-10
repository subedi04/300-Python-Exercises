'''
Write a Python Program to Open the URL using other than urllib library
'''

import requests

# Replace 'https://example.com' with the URL you want to open
url = 'https://example.com'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the content of the response (HTML content of the webpage)
        print(response.text)
    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
