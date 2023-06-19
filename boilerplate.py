from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_boilerplate_code(url):
    service_obj = Service("c:/Users/hafim/SeleniumDrivers/chromedriver.exe")
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service_obj, options=options)

    driver.get(url)
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type="button"][aria-haspopup="true"]'))
    )
    dropdown.click()

    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[text()="Python3"]'))
    )
    option.click()

    # Initialize an empty list to store the lines of code
    code = []

    # Find all the lines of code
    time.sleep(2) 
    lines_of_code_elements = driver.find_elements(By.CLASS_NAME, 'view-line')

    # Iterate through the lines of code
    for line_element in lines_of_code_elements:
        # Find all the span elements inside this line which are children of another span
        span_elements = line_element.find_elements(By.XPATH, './/span/span')

        # Get the text content of each span and concatenate them to get the line of code
        line_of_code = ''.join(span.text for span in span_elements)

        code.append(line_of_code)

    # Now, `code` is a list of strings, each string being a line of code.
    # If you want the code as a single string with line breaks, you can join the lines like this:
    code_str = '\n'.join(code)

    return code_str
