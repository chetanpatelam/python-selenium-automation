from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# If you get deprecation warning and it is not harmful, but gives warning messages,
# import warnings then  warning.filterwarning("ignore", category = type of warning to be ignored).

import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)

# init driver
driver = webdriver.Chrome(executable_path='c://Users/chait/automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')
#search.send_keys('Ring Camera System')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#assert 'ring' or 'camera' or 'system' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
