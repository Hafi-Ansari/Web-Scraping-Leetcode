from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_obj = Service("c:/Users/hafim/SeleniumDrivers/chromedriver.exe")
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://leetcode.com/problemset/all/")
time.sleep(5)

# Find all the question links on the page
question_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'h-5')]")

# Extract the href attribute from each link and store them in a list
links_list = [link.get_attribute("href") for link in question_links]

# Close the browser
driver.quit()

# Save the links to a text file
with open("leetcode_links.txt", "w") as file:
    for link in links_list:
        file.write(link + "\n")

print("LeetCode question links have been saved to leetcode_links.txt.")