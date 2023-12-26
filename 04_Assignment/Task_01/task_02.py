'''
Create a web scraping tool that extracts data from 
a website and saves it to a CSV file using Python 
libraries such as Requests, BeautifulSoup, and Pandas.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save_to_csv(url, csv_filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the webpage (modify this part based on the structure of the webpage)
        data_list = []
        for item in soup.find_all('div', class_='your-target-class'):
            # Modify the code to extract specific data based on the structure of the webpage
            title = item.find('h2').text.strip()
            description = item.find('p').text.strip()
            data_list.append({'Title': title, 'Description': description})

        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data_list)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}")
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the website you want to scrape
    website_url = input("Enter the URL of the website to scrape: ")

    # Replace 'output.csv' with the desired CSV file name
    csv_file = input("Enter the name of the CSV file to save data: ")

    scrape_and_save_to_csv(website_url, csv_file)
