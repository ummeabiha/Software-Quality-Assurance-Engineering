from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from CommonUtils import CommonUtils

class ResetPswdPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/reset-password'
        self.xPaths_Link = [
            ["//a[text()='Do not have an account? Signup!']", 'http://localhost:5173/bytebazaar/signup']
        ]
        self.error_messages = [
            '400: "password" should contain at least 1 lower-cased letter',
            '400: "password" should contain at least 1 upper-cased letter',
            '400: "password" should contain at least 1 number',
            '400: "password" should contain at least 1 symbol',
            '400: "password" should be at least 8 characters long',
            '400: Passwords do not match',
            '400: "email" must be a valid email',
            '404: undefined',
            'Password have been changed successfully',
        ]

    def open(self):
        self.driver.get(self.url)

    def test_form_submission(self, email, password, confirmPassword):
        try:
            email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            confirmPassword_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            CommonUtils.clear_and_send_keys(email_input, email)
            CommonUtils.clear_and_send_keys(password_input, password)
            CommonUtils.clear_and_send_keys(confirmPassword_input, confirmPassword)
            
            submit_button.click()

            return (CommonUtils.handle_toasts(self.driver))
        except TimeoutException:
            return "Error: Timeout occurred while waiting for element"
