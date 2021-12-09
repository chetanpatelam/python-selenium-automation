from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

search = driver.find_element(By.CSS_SELECTOR, '#nav-cart span.nav-cart-icon').click()

# Amazon Logo
actual_answer = driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
expected_answer = "Your Amazon Cart is empty"

if actual_answer == expected_answer:
    print(actual_answer)
    print('Test Passed')
else:
    print('Test Failed')

sleep(4)
driver.quit()
