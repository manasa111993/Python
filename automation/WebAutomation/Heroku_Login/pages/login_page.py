from selenium.webdriver.common.by import By

from Heroku_Login.locators.locators import LoginLocators
from Heroku_Login.pages.base_page import BasePage


#from automation.WebAutomation.Heroku_Login.locators.locators import LoginLocators
#from automation.WebAutomation.Heroku_Login.pages.base_page import BasePage


class HerokuLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #self.username_field = (By.ID, "username")
        #self.password_field = (By.ID, "password")
        #self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        #self.flash_message = (By.ID, "flash")

    def open(self,url):
        self.driver.get(url)

    def enter_username(self, username):
        self.send_keys(LoginLocators.username_field, username)

    def enter_password(self, password):
        self.send_keys(LoginLocators.password_field, password)

    def click_login(self):
        self.click(LoginLocators.login_button)

    def get_flash_message(self):
        return self.get_text(LoginLocators.flash_message)



