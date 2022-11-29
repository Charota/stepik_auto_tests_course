from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    
    browser.find_element(By.CSS_SELECTOR, 'button#book').click()

    time.sleep(1.5)

    value = int(browser.find_element(By.CSS_SELECTOR, 'span#input_value').text)
    
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(math.log(abs(12*math.sin(value))), math.e)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    time.sleep(20)
    browser.quit()