import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BaseClass


class Login(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def login_to_amazon(self,email,password):
        self.click("login_xpath")
        self.input_text("email_xpath",email)
        self.click("continue_xpath")
        self.input_text("pass_xpath",password)
        self.click("signIn_xpath")
