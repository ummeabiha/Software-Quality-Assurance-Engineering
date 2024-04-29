from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.common.exceptions import NoAlertPresentException

logging.basicConfig(level=logging.INFO)

class DeleteProdsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/admin/manage-inventory'

    def open(self):
        self.driver.get(self.url)

    def dismiss_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException:
            print("<span style='color: red;'>No Alert Found.</span><br>")

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("<span style='color: red;'>No Alert Found.</span><br>")

    def check_product_quantity(self, total_prods):
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        return total_prods == len(rows)

    def perform_delete_action(self):
        delete_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr/td/button[contains(@class, 'delete-btn')]")))
        delete_btn.click()

    def test_delete_product(self):
        total_prods = 3

        self.perform_delete_action()
        self.dismiss_alert()

        time.sleep(3) 

        if self.check_product_quantity(total_prods):
            print("Test case 1 passed: On Dismiss Delete, Products quantity did not decrease.<br>")
        else:
            print("<span style='color: red;'>Test case 1 failed: Product quantity decreased on unsuccessful delete.</span><br>")

        self.perform_delete_action()
        self.accept_alert()

        time.sleep(3) 

        if self.check_product_quantity(total_prods-1):
            print("Test case 2 passed: On Successful Delete, Products quantity decreased.<br>")
        else:
            print("<span style='color: red;'>Test case 2 failed: Product quantity did not decrease on successful delete.</span><br>")
