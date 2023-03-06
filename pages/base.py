from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (StaleElementReferenceException,
                                        ElementClickInterceptedException,
                                        TimeoutException)
from selenium.webdriver.common.by import By


class BasePage(object):
    """Класс предоставляющий методы для взаимодействия с драйвером"""

    def __init__(self, driver):
        self.driver = driver
        self.overlay = (By.XPATH, "//div[@id='overlay']")
        self.popup_window = (By.XPATH, "//div[@class='modal-content']")
        self.popup_ok_btn = (By.XPATH, "//button[@type='submit']")

    def wait_element_present(self, locator: tuple, timeout=25) -> WebElement:
        """
        Ожидание представление элемента.

        :param locator: Локатор элемента.
        :param timeout: Ожидание элемента.
        :return: Элемент возвращения данных после выполнения ожидания.
        """
        return WebDriverWait(self.driver, timeout, ignored_exceptions=StaleElementReferenceException) \
            .until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator: tuple, timeout=25) -> True or TimeoutException:
        """
        Ожидание клика по элементу.

        :param locator:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout, ignored_exceptions=ElementClickInterceptedException) \
            .until(EC.element_to_be_clickable(locator))

    def click_element(self, locator: tuple, timeout=25) -> True or TimeoutException:
        """
        Выбор элемента.

        :param locator:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout, ignored_exceptions=ElementClickInterceptedException) \
            .until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator: tuple or WebElement) -> WebElement:
        """
        Поиск элемента.

        :param by: Метод поиска элемента.
        :param locator: Локатор элемента.
        :return: Элемент возвращения данных после поиска..
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple or WebElement) -> List[WebElement]:
        """
        Поиск элементов.

        :param by:
        :param locator:
        :return:
        """
        return self.driver.find_elements(*locator)

    def get_element_text(self, locator: tuple or WebElement) -> str:
        """
        
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            return self.wait_element_present(locator).text
        elif isinstance(locator, WebElement):
            return locator.text

    def wait_invisibility(self, locator: tuple, timeout=25) -> True or TimeoutException:
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def wait_text_in_element(self, locator: tuple, text: str, timeout=25) -> True or TimeoutException:
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def send_value_by_input_text(self, locator: WebElement, value: str):
        return self.wait_element_present(locator).send_keys(value)

    def check_element_for_activity(self, locator: tuple or WebElement) -> True:
        return self.find_element(locator).is_enabled()
