import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the title of the webpage
title = soup.title.string
print(f"Title of the webpage: {title}")
