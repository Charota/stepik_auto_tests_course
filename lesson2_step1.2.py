from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chestImg = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    chestImgValuex = chestImg.get_attribute('valuex')

    inputAnswer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    inputAnswer.send_keys(calc(chestImgValuex))

    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(20)
    browser.quit()