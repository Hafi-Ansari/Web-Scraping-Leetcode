from bs4 import BeautifulSoup
import requests

# Make a request to the website
r = requests.get("https://leetcode.com/problems/two-sum/")

# Parse the HTML of the page
soup = BeautifulSoup(r.text, 'html.parser')

# Extract all the text
text = soup.get_text()

# Print the text
print(text)
