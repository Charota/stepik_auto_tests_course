from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_val = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text

    inputField = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    inputField.send_keys(calc(x_val))

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()

    radioBtn = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radioBtn.click()

    submitBtn = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submitBtn.click()

finally:
    time.sleep(20)
    browser.quit()