from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_input = (By.XPATH, "//form[@id='email-form']//input[@placeholder='Please enter your email']")
        self.continue_btn = (By.XPATH, "//form[@id='email-form']//button[@type='submit']")
        self.password_input = (By.XPATH, "//form[@id='password-form']//input[@name='password']")
        self.sign_in_btn = (By.XPATH, "//form[@id='password-form']//button[@type='submit']")

    def do_login(self, user):
        self.send_value_by_input_text(self.login_input, user.get('login'))
        self.click_element(self.continue_btn)
        self.wait_element_present(self.password_input)
        self.send_value_by_input_text(self.password_input, user.get('password'))
        self.click_element(self.sign_in_btn)
        return self
