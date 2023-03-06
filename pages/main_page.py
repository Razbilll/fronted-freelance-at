import pytest
from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_btn = (By.XPATH, "//button[contains(@class, 'filter-btn')]")
        self.filter_input_text = (By.XPATH, "//input[@placeholder='Id or Name']")
        self.study_element = (By.XPATH, "//div[@id='studies']/div[contains(@class,'flex-grow')]")
        self.study_title = (By.CSS_SELECTOR, "div.box-title span[class*=tipped]")
        self.ract_btn = (By.XPATH, "//div[@class='row-flex']//i[@class='fa fa-files-o']")
        self.next_page_btn = (By.XPATH, "//div[@class='studies-pagination']//li[last()]/a")

    def open_filter(self):
        self.click_element(self.filter_btn)
        return self

    def find_and_open_ract_study(self, study_name: str):
        self.open_filter()
        self.send_value_by_input_text(self.filter_input_text, study_name)
        self.click_element(self.popup_ok_btn)
        self.wait_invisibility(self.overlay)
        while next_btn_is_enabled := len(self.find_elements(self.next_page_btn)) \
                                     or len(self.find_elements(self.study_element)):
            studies = self.find_elements(self.study_element)
            for study in studies:
                study_text = study.find_element(*self.study_title).text.partition('—')[2].strip()
                if study_text == study_name:
                    study.find_element(*self.ract_btn).click()
                    self.wait_invisibility(self.overlay)
                    return self
            if next_btn_is_enabled:
                self.click_element(self.next_page_btn)
                self.wait_invisibility(self.overlay)
        pytest.fail(f"Study '{study_name}' not found!")


