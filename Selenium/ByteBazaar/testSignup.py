from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# # Enable headless mode
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')  

logging.basicConfig(level=logging.INFO)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost:5173/bytebazaar/signup')

error_messages = [
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

xPaths_Link = [
    ["//button[span[text()='Sign Up with Google']]", 'https://accounts.google.com/'],
    ["//a[text()='Forgot Password?']", 'http://localhost:5173/bytebazaar/forgot-password'],
    ["//a[text()='Already have an account? Login!']", 'http://localhost:5173/bytebazaar/login']
]

print(driver.title)

def check_toast_message(test_num, expected_message, toast_message):
    if expected_message in toast_message:
        logging.info(f"Test case '{test_num}' passed: Expected toast message '{expected_message}' received")
    else:
        logging.error(f"Test case '{test_num}' failed: Expected toast message '{expected_message}' not received. Actual: {toast_message}")

def clear_and_send_keys(element, keys):
    element.clear()
    element.send_keys(keys)
    time.sleep(0.5)  

def test_form_submission(firstName, lastName, email, password, confirmPassword):
    first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
    last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    confirm_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    clear_and_send_keys(first_name_input, firstName)
    clear_and_send_keys(last_name_input, lastName)
    clear_and_send_keys(email_input, email)
    clear_and_send_keys(password_input, password)
    clear_and_send_keys(confirm_password_input, confirmPassword)

    submit_button.click()

    toast_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))

    toast_message = toast_element.text

    if toast_element.is_displayed():
        close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Toastify']//button[@aria-label='close']")))
        close_button.click()

    return toast_message


# Testing Navigation Links on Signup Form
def navigation_test_status(expected_url):
    current_url = driver.current_url

    if (expected_url == current_url) or (expected_url in current_url):
        logging.info(f"Test case passed: URL navigation occurred to {expected_url}.")
    else:
        logging.error("Test case failed: URL navigation did not occur.")
    
    time.sleep(1)
    driver.back()

def test_navigation_links():
    print("\nRunning Tests for Navigation Links")
    for xpath, expected_url in xPaths_Link:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
        navigation_test_status(expected_url)
        print("\n")


# RUN TEST CASES
def run_test_cases():
    with open('./ByteBazaar/TestDataFiles/testSignupData.txt', 'r') as file:
        print("\nRunning Tests for Signup Form")
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            firstName, lastName, email, password, confirmPassword = data
            toast_message = test_form_submission(firstName, lastName, email, password, confirmPassword)
            logging.info(f"Submitting form with data: {data}")
            logging.info(f"Toast message: {toast_message}")
            check_toast_message(lines.index(line) + 1, error_messages[lines.index(line)], toast_message)
            print("\n") 
    
    time.sleep(2)
    test_navigation_links()

run_test_cases()
time.sleep(1)
driver.quit()
