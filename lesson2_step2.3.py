from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('test')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('test')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('test')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:

    time.sleep(20)
    browser.quit()