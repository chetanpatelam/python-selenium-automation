from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

#Finds Cart button and clicks on it.
driver.find_element(By.CSS_SELECTOR, '#nav-cart span.nav-cart-icon').click()


# Verifies the status of the cart and store in actual_answer variable
actual_answer = driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
expected_answer = "Your Amazon Cart is empty"


# Verifies if actual answer and expected answer are same
assert actual_answer == expected_answer, f'f Expected {expected_answer}, but got {actual_answer}'
sleep(4)


print('We expected :"'+expected_answer+'" and got :"'+actual_answer+'".')
print('Test Passed')

driver.quit()
