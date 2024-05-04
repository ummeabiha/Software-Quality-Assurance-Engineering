from selenium.webdriver.common.by import By
from CommonUtils import CommonUtils

class ForgotPswdPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/forgot-password'
        self.xPaths_Link = [
            ["//a[text()='Do not have an account? Signup!']", 'http://localhost:5173/bytebazaar/signup']
        ]
        self.error_messages = [
            "Error User Does Not Exist!!",
            "Error User Does Not Exist!!",
            "OTP verification code has been sent to your registered email"
        ]

    def open(self):
        self.driver.get(self.url)

    def test_form_submission(self, email):
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        CommonUtils.clear_and_send_keys(email_input, email)
        
        submit_button.click()

        return (CommonUtils.handle_toasts(self.driver))
        

