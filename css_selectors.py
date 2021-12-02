from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Amazon Logo
amazon_logo = driver.find_element(By.CSS_SELECTOR, "a.a-link-nav-icon i.a-icon.a-icon-logo")

# Create Account Text
amazon_create_text = driver.find_element(By.CSS_SELECTOR, "div.a-box-inner h1.a-spacing-small")

customer_name = driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

customer_mail = driver.find_element(By.CSS_SELECTOR, "#ap_email")

customer_pass = driver.find_element(By.CSS_SELECTOR, "#ap_password")

customer_pass_verify = driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

customer_auth = driver.find_element(By.CSS_SELECTOR, "#auth-continue-announce")

customer_noti_of_cond = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

customer_priv_noti = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

customer_sign_in = driver.find_element(By.CSS_SELECTOR, "div.a-row a[href*='/ap/signin?openid.pape.max_auth_age']")

#expected_text = 'Amazon'


# verify
#assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'

sleep(4)

print('Test Passed')

driver.quit()

