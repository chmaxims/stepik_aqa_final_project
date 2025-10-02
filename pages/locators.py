from selenium.webdriver.common.by import By


class MainPageLocators():
    # LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    MESSAGE_ALERT_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1)")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

# class ProductPageLocators():
#
