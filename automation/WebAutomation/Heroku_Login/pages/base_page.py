from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).clear()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))