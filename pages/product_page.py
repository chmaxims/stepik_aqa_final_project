from .base_page import BasePage
from pages.locators import MainPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_message_alert_price()
        self.check_message_alert_book_name()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_message_alert_price(self):
        message_alert_book_price = self.browser.find_element(*MainPageLocators.MESSAGE_ALERT_PRICE)
        book_price = self.browser.find_element(*MainPageLocators.BOOK_PRICE)
        assert message_alert_book_price.text == book_price.text

    def check_message_alert_book_name(self):
        message_alert_book_name = self.browser.find_element(*MainPageLocators.MESSAGE_ALERT_BOOK_NAME)
        book_name = self.browser.find_element(*MainPageLocators.BOOK_NAME)
        assert message_alert_book_name.text == book_name.text
