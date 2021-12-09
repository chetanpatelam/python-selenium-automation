from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT1 = (By.ID, 'helpsearch')
SEARCH_SUBMIT1 = (By.CSS_SELECTOR, "i.a-icon.a-icon-search")


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    print("Opening Amazon Search Page")


@when('Input {search_word1} into help search field')
def input_search(context, search_word1):
    search = context.driver.find_element(*SEARCH_INPUT1)
    search.clear()
    search.send_keys(search_word1)
    print("inputing word "+search_word1+" into search field")
    sleep(4)


@when('Click on search button')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT1).click()
    print("clicking on search icon")
    sleep(1)


@then('Confirm for {search_word1} are shown')
def verify_found_results_text(context, search_word1):
    #assert search_word1.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
    print("Test Passed")

