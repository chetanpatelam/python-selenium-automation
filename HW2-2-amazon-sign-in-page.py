from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

driver.find_element(By.XPATH, "//i[contains(@class, 'a-icon a-icon-logo')]")
driver.find_element(By.ID, 'ap_email')
#driver.find_element(By.ID, 'ap_cred')
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//div[@id='legalTextRow'] "
                              "//a[contains (@href, 'signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//div[@id='legalTextRow'] "
                              "//a[contains (@href, 'ap_signin_notification_privacy_notice')]")

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, 'createAccountSubmit')

sleep(4)

print('Test Passed')
driver.quit()
