import requests
from bs4 import BeautifulSoup, Tag

# URL of the Leetcode problem
url = 'https://leetcode.com/problems/permutations/'

# Send a GET request
response = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with the problem description
problem_div = soup.find('div', class_='_1l1MA')

# Initialize a list to hold all parts of the problem description
problem_description_parts = []

# Iterate over all direct children of the problem_div
for child in problem_div.children:
    if isinstance(child, Tag):  # only process if the child is a Tag object
        if child.name == 'p':
            # For paragraphs, just get the text
            problem_description_parts.append(child.get_text(separator=' '))
        elif child.name == 'pre':
            # For preformatted text (like examples), preserve newlines
            problem_description_parts.append(child.get_text())
        elif child.name == 'ul':
            # For unordered lists (like constraints), add each list item on a new line
            list_items = [li.get_text() for li in child.find_all('li')]
            problem_description_parts.append('\n'.join(list_items))

# Join all parts of the problem description with double newlines
problem_description = '\n\n'.join(problem_description_parts)

print(problem_description)
