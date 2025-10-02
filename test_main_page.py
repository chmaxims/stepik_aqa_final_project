import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url) # выполняем метод страницы - переходим на страницу логина
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page_login = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    basket_page = BasketPage(browser, link)
    page.open()
    basket_page.view_basket_header()
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_about_empty_basket()






# def test_guest_should_see_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#





