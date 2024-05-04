from selenium.webdriver.common.by import By
from CommonUtils import CommonUtils

class UserSignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/signup'
        self.xPaths_Link = [
            ["//button[span[text()='Sign Up with Google']]", 'https://accounts.google.com/'],
            ["//a[text()='Forgot Password?']", 'http://localhost:5173/bytebazaar/forgot-password'],
            ["//a[text()='Already have an account? Login!']", 'http://localhost:5173/bytebazaar/login']
        ]
        self.error_messages = [
            '"password" should contain at least 1 lower-cased letter',
            '"password" should contain at least 1 upper-cased letter',
            '"password" should contain at least 1 number',
            '"password" should contain at least 1 symbol',
            '"password" should be at least 8 characters long',
            'Passwords do not match',
            'User with given email already exists',
            '"email" must be a valid email',
            "Signup successful! Please Log In."
        ]

    def open(self):
        self.driver.get(self.url)
        
    def test_form_submission(self, firstName, lastName, email, password, confirmPassword):
        first_name_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
        last_name_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        confirm_password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        CommonUtils.clear_and_send_keys(first_name_input, firstName)
        CommonUtils.clear_and_send_keys(last_name_input, lastName)
        CommonUtils.clear_and_send_keys(email_input, email)
        CommonUtils.clear_and_send_keys(password_input, password)
        CommonUtils.clear_and_send_keys(confirm_password_input, confirmPassword)

        submit_button.click()

        return(CommonUtils.handle_toasts(self.driver))

