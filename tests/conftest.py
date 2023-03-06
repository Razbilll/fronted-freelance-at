import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from dotenv import load_dotenv

from pages.login import LoginPage
from pages.main_page import MainPage
from data.test_data import Authorization

load_dotenv()


def get_main_page(driver):
    """Метод выполняющий авторизацию на сайте для фикстуры."""
    login_page = LoginPage(driver)
    login_page.do_login(Authorization.get_user(Authorization.global_admin))
    main_page = MainPage(driver)
    main_page.wait_invisibility(main_page.overlay)
    return driver


def get_driver(request):
    #user_language = request.config.getoption("language")
    options = Options()
    #options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(os.getenv("BASE_URL"))
    return driver


@pytest.fixture(scope="class")
def driver_class_scope(request):
    driver = get_driver(request)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def main_page_class_scope(driver_class_scope):
    get_main_page(driver_class_scope)
    return MainPage(driver_class_scope)
