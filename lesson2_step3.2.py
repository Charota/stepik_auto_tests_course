from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(1.5)

    browser.switch_to.window(browser.window_handles[1])

    value = int(browser.find_element(By.CSS_SELECTOR, 'span#input_value').text)
    print(value)
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(math.log(abs(12*math.sin(value))), math.e)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(20)
    browser.quit()