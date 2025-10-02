from .base_page import BasePage
from pages.locators import MainPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.message_alert_price()
        self.message_alert_book_name()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def message_alert_price(self):
        message_alert_book_price = self.browser.find_element(*MainPageLocators.MESSAGE_ALERT_PRICE)
        book_price = self.browser.find_element(*MainPageLocators.BOOK_PRICE)
        assert message_alert_book_price.text == book_price.text, f'expected price "{book_price.text}", got "{message_alert_book_price.text}"'

    def message_alert_book_name(self):
        message_alert_book_name = self.browser.find_element(*MainPageLocators.MESSAGE_ALERT_BOOK_NAME)
        book_name = self.browser.find_element(*MainPageLocators.BOOK_NAME)
        assert message_alert_book_name.text == book_name.text, f'expected: name "{book_name.text}", actual: "{message_alert_book_name.text}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message is still present, but it was expected to disappear"

    # def link(self):
    #     link = self.browser.find_element(*MainPageLocators.LINK)