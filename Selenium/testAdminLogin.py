from webDriverSetup import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.INFO)

driver = get_chrome_driver()
driver.get('http://localhost:5173/bytebazaar/admin-login')

error_messages = [
    '"email" is not allowed to be empty',
    'Admin not Registered!',
    'Invalid Email or Password',
    '"email" must be a valid email',
    'Login successful!',
]

print("Title: ", driver.title)

def check_toast_message(test_num, expected_message, toast_message):
    if expected_message in toast_message:
        logging.info(f"Test case '{test_num}' passed: Expected toast message '{expected_message}' received")
    else:
        logging.error(f"Test case '{test_num}' failed: Expected toast message '{expected_message}' not received. Actual: {toast_message}")

def clear_and_send_keys(element, keys):
    element.clear()
    element.send_keys(keys)
    time.sleep(0.5)

def handle_toasts():
    toast_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))

    toast_message = toast_element.text

    if toast_element.is_displayed():
        close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Toastify']//button[@aria-label='close']")))
        close_button.click()

    return toast_message

def test_form_submission(email, password):
    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    clear_and_send_keys(email_input, email)
    clear_and_send_keys(password_input, password)

    submit_button.click()

    toast_message= handle_toasts()
    return toast_message
   

def direct_login_click():
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    toast_message = handle_toasts()
    logging.info(f"Toast message: {toast_message}")
    check_toast_message(1, error_messages[0], toast_message)
    print("\n")

# RUN TEST CASES
def run_test_cases():
    print("\nRunning Tests for Admin Login Form")
    direct_login_click()
    with open('./TestDataFiles/testAdminLoginData.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            email, password = data
            toast_message = test_form_submission(email, password)
            logging.info(f"Submitting form with data: {data}")
            logging.info(f"Toast message: {toast_message}")
            check_toast_message(lines.index(line) + 2, error_messages[lines.index(line)+1], toast_message)
            print("\n")

    time.sleep(1)
    driver.back()

run_test_cases()

time.sleep(1)
driver.quit()
