from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_CLICK = (By.CSS_SELECTOR, '#nav-cart span.nav-cart-icon')
CART_COUNT = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")


@given('Open Amazon Home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    print("Opening Amazon Home Page")


@when('Press on Cart icon')
def press_cart(context):
    search = context.driver.find_element(*CART_CLICK)
    search.click()
    #search.clear()
    print("Clicked on Cart icon")
    sleep(4)


@then('Confirm that the cart is empty')
def verify_found_results_text(context):
    cart = context.driver.find_element(*CART_COUNT).text
    #search.clear()
    assert cart == "Your Amazon Cart is empty", f"Your Amazon Cart is empty expected but got, {cart}"
    print("Test Passed")

