# This file contains test cases for login functionality.
import pytest

#from automation.WebAutomation.Heroku_Login.Data.data_file import herokuData
#from automation.WebAutomation.Heroku_Login.Data.data_file import herokuData
#from automation.WebAutomation.Heroku_Login.pages.login_page import HerokuLoginPage

from Heroku_Login.Data.data_file import herokuData
from Heroku_Login.pages.login_page import HerokuLoginPage
import allure

@allure.feature("Heroku Login Tests")
#@pytest.mark.usefixtures("invoke_browser")
class TestLogin:
    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, invoke_browser):
        """Test case for a valid login."""
        driver = invoke_browser
        login_page = HerokuLoginPage(driver)
        login_page.open(herokuData["url"])
        login_page.enter_username(herokuData["username"])
        login_page.enter_password(herokuData["password"])
        login_page.click_login()
        assert "You logged into a secure area!" in login_page.get_flash_message()


    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self, invoke_browser):
        driver = invoke_browser
        """Test case for an invalid login."""
        login_page = HerokuLoginPage(driver)
        login_page.open(herokuData["url"])
        login_page.enter_username(herokuData["wrong_user"])
        login_page.enter_password(herokuData["wrong_password"])
        login_page.click_login()
        assert "Your username is invalid!" in login_page.get_flash_message()
