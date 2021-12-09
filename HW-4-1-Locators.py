from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

#1st Tab - With and without use of and text()
tab1 = driver.find_element(By.XPATH, "//a[contains(@href,'/gp/bestsellers/ref=zg_bs_tab')]").text
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/bestsellers/ref=zg_bs_tab') and text()='Best Sellers']")


#2nd Tab - With and without use of and text()
tab2 = driver.find_element(By.XPATH,"//a[@href='/gp/new-releases/ref=zg_bs_tab']").text
driver.find_element(By.XPATH,"//a[@href='/gp/new-releases/ref=zg_bs_tab' and text()='New Releases']")


#3rd Tab - With and without use of and text()
tab3 = driver.find_element(By.XPATH,"//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']").text
driver.find_element(By.XPATH,"//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab' and text()='Movers & Shakers']")


#4th Tab - With and without use of and text()
tab4 = driver.find_element(By.XPATH,"//a[@href='/gp/most-wished-for/ref=zg_bs_tab']").text
driver.find_element(By.XPATH,"//a[@href='/gp/most-wished-for/ref=zg_bs_tab' and text()='Most Wished For']")


#5th Tab - With and without use of and text()
tab5 = driver.find_element(By.XPATH,"//a[@href='/gp/most-gifted/ref=zg_bs_tab']").text
driver.find_element(By.XPATH,"//a[@href='/gp/most-gifted/ref=zg_bs_tab' and text()='Gift Ideas']")


sleep(4)
print(tab1)
print(tab2)
print(tab3)
print(tab4)
print(tab5)
print('Test Passed')
driver.quit()
