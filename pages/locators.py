from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    MESSAGE_ALERT_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1)")
    VIEW_BASKET_BUTTON_HEADER = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_INFO = (By.CSS_SELECTOR, "#content_inner>p")