from selenium.webdriver.common.by import By
from CommonUtils import CommonUtils

class UserLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/login'
        self.xPaths_Link = [
            ["//button[span[text()='Login with Google']]", 'https://accounts.google.com/'],
            ["//a[text()='Forgot Password?']", 'http://localhost:5173/bytebazaar/forgot-password'],
            ["//a[text()='Do not have an account? Signup!']", 'http://localhost:5173/bytebazaar/signup']
        ]
        self.error_messages = [
            'Invalid Email or Password',
            '"email" must be a valid email',
            '"email" must be a valid email',
            'Login successful!',
        ]

    def open(self):
        self.driver.get(self.url)

    def test_form_submission(self, email, password):
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        CommonUtils.clear_and_send_keys(email_input, email)
        CommonUtils.clear_and_send_keys(password_input, password)

        submit_button.click()

        return(CommonUtils.handle_toasts(self.driver))

