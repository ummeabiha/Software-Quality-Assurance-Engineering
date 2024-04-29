from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class CommonUtils:
    @staticmethod
    def clear_and_send_keys(element, keys):
        element.clear()
        element.send_keys(keys)
        
    @staticmethod
    def handle_toasts(driver):
        toast_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
        toast_message = toast_element.text

        if toast_element.is_displayed():
            close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Toastify']//button[@aria-label='close']")))
            close_button.click()

        return toast_message

    @staticmethod
    def check_toast_message(test_num, expected_message, toast_message):
        if toast_message is None:
            return
        elif expected_message in toast_message:
            print(f"Test case '{test_num}' passed: Expected toast message '{expected_message}' received.<br>")
        else:
            print(f"<span style='color: red;'>Test case '{test_num}' failed: Expected toast message '{expected_message}' not received. Actual: {toast_message}</span><br>")

    @staticmethod
    def page_refresh(driver, test_no, page, submit_btn):
        try:
            WebDriverWait(driver, 1).until(EC.staleness_of(submit_btn)) 
            print(f"Test case {test_no} passed: {page} is Successful, and Page refresh occured.<br>")

        except TimeoutException:
            print(f"<span style='color: red;'>Test case {test_no} failed.</span><br>")
            return None
    
    @staticmethod
    def navigation_test_status(driver, expected_url):
        current_url = driver.current_url

        if (expected_url == current_url) or (expected_url in current_url):
            print(f"Test case passed: URL navigation occurred to {expected_url}.<br>")
        else:
            print("<span style='color: red;'>Test case failed: URL navigation did not occur.</span><br>")

        driver.back()


