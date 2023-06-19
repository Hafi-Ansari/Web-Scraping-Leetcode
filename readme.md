Project Title: Leetcode Questions Web Scraper 

Project Description: This is a Python application that lets you parse Leetcode questions and retrieve their Title, Description, Test Examples, Constraints, Boilerplate Code from the Code Editor, and Test Cases using Selenium and BeautifulSoup4. 

Installation: pip install selenium, pip install python, pip install beautifulsoup4, pip install pymongo

Usage: To use, put the URL of any Leetcode questions you want parsed into leetcode.txt. Then, run populate.py. This will populate questions.json with JSON objects containing all the Leetcode information. From here you can run database.py to send the JSON objects as documents to MongoDB (modify the connection string and client of course). 

If you want to load the first 50 Leetcode questions into the leetcode.txt file, run questions.py. You can also change the link to any of Leetcode's curated (free) lists by changing the link in driver.get(). Replace "os.getenv(SERVICE_OBJ_PATH") in service_obj = Service(os.getenv("SERVICE_OBJ_PATH")) with your path to your downloaded Chrome driver. 

If you want to modify the language the code editor returns, change "Python3" in EC.element_to_be_clickable((By.XPATH, '//div[text()="Python3"]')) to your desired language in boilerplate.py. 

Configuration: You will need to download a Chrome driver that closely matches your Chrome version. This program runs on pip 23.1.2, selenium version 4.10.0, beautifulsoup version: 4.12.2, pymongo 4.3.3. 