from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    print(x)
    fVal = math.log(abs(12*math.sin(x)), math.e)
    print(fVal)
    input = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)

    input.send_keys(fVal)

    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
finally:

    time.sleep(20)
    browser.quit()