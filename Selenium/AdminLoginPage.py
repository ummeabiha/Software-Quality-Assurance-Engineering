from selenium.webdriver.common.by import By
from CommonUtils import CommonUtils

class AdminLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/admin-login'
        self.error_messages = [
            '"email" is not allowed to be empty',
            'Admin not Registered!',
            'Invalid Email or Password',
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

        toast_message = CommonUtils.handle_toasts(self.driver)
        return toast_message
