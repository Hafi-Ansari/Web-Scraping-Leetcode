from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service_obj = Service("c:/Users/hafim/SeleniumDrivers/chromedriver.exe")
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://leetcode.com/problemset/all/")



