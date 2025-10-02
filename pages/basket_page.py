from pages.base_page import BasePage
from pages.locators import BasketPageLocators, MainPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert  self.is_element_present(*BasketPageLocators.BASKET_INFO), 'Basket is not empty'

    def view_basket_header(self):
        add_to_basket_button_header = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON_HEADER)
        add_to_basket_button_header.click()

    def should_be_text_about_empty_basket(self):
        actual_text = self.browser.find_element(*BasketPageLocators.BASKET_INFO).text
        assert "Your basket is empty" in actual_text, f"Expected 'Your basket is empty' not found in: '{actual_text}'"