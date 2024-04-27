from webDriverSetup import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

from selenium.common.exceptions import TimeoutException

logging.basicConfig(level=logging.INFO)

driver = get_chrome_driver()
driver.get('http://localhost:5173/bytebazaar/admin/manage-inventory')

error_messages = [
    'Product Name must not exceed 30 characters.',
    'Product Description must not exceed 200 characters.',
    'Product Category must not exceed 20 characters.',
    'Product Brand must not exceed 20 characters.',
    'Product Price must be a positive number.',
    'Product Rating must be a positive number.',
    'Edit is Successful.',
]


def check_toast_message(test_num, expected_message, toast_message):
    if toast_message is None:
        return
    elif expected_message in toast_message:
        logging.info(f"Test case '{test_num}' passed: Expected toast message '{expected_message}' received")
    else:
        logging.error(f"Test case '{test_num}' failed: Expected toast message '{expected_message}' not received. Actual: {toast_message}")

def clear_and_send_keys(element, keys):
    """Clears an input element and sends keys to it."""
    element.clear()
    element.send_keys(keys)
    #time.sleep(0.5)


def test_form_submission(name, price, image, category, brand, rating, description):
    """Submits a form with given data and returns the toast message."""
    name_input = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    price_input = driver.find_element(By.CSS_SELECTOR, "input[name='price']")
    image_input = driver.find_element(By.CSS_SELECTOR, "input[name='image']")
    category_input = driver.find_element(By.CSS_SELECTOR, "input[name='category']")
    brand_input = driver.find_element(By.CSS_SELECTOR, "input[name='brand']")
    rating_input = driver.find_element(By.CSS_SELECTOR, "input[name='rating']")
    description_input = driver.find_element(By.CSS_SELECTOR, "textarea[name='description']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    clear_and_send_keys(name_input, name)
    clear_and_send_keys(price_input, price)
    clear_and_send_keys(image_input, image)
    clear_and_send_keys(category_input, category)
    clear_and_send_keys(brand_input, brand)
    clear_and_send_keys(rating_input, rating)
    clear_and_send_keys(description_input, description)
    submit_button.click()

    try:
        toast_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
        toast_message = toast_element.text

        if toast_element.is_displayed():
            close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Toastify']//button[@aria-label='close']")))
            close_button.click()
        return toast_message
    
    except TimeoutException:
        logging.error("Timeout: Toast message not displayed.")
        
        try:
            WebDriverWait(driver, 3).until(EC.staleness_of(submit_button)) 
            logging.info("Page Refresh Occured")
            logging.info(f"Test case 7 passed: Edit is Successful!")
        except TimeoutException:
            logging.error(f"Test case 7 failed.")

        return None
    

# RUN TEST CASES
def run_test_cases():
    with open('./ByteBazaar/TestDataFiles/testEditProdData.txt', 'r') as file:
        print("\nRunning Tests for Edit Products Form")
        lines = file.readlines()

        edit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "edit-btn")))
        edit_button.click()

        for line in lines:
            data = line.strip().split(',')
            name, price, image, category, brand, rating, description = data
            toast_message= test_form_submission(name, price, image, category, brand, rating, description)
            logging.info(f"Submitting form with data: {data}")
            if (toast_message !=None):
                logging.info(f"Toast message: {toast_message}")
                check_toast_message(lines.index(line) + 1, error_messages[lines.index(line)], toast_message)
                print("\n")

run_test_cases()
time.sleep(1)
driver.quit()
