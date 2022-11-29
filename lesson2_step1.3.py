from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, 'span#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, 'span#num2').text

    Select(browser.find_element(By.CSS_SELECTOR, 'select#dropdown')).select_by_value(str(int(num1)+int(num2)))

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
finally:

    time.sleep(20)
    browser.quit()