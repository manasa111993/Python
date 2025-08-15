from selenium.webdriver.common.by import By

class LoginLocators:
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    flash_message = (By.ID, "flash")
