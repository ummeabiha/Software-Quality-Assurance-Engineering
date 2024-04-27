from webDriverSetup import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from selenium.common.exceptions import NoAlertPresentException

logging.basicConfig(level=logging.INFO)

driver = get_chrome_driver()
driver.get('http://localhost:5173/bytebazaar/admin/manage-inventory')

print("Title: ", driver.title)

total_prods = 5

# Locate the table by tag name 'table'
table = driver.find_element(By.TAG_NAME, 'table')
rows = table.find_elements(By.XPATH, "./tbody/tr")

# Wait for delete button to be present
delete_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td/button[contains(@class, 'delete-btn')]")))
delete_btn.click()

# Dismiss the alert if present
try:
    alert = driver.switch_to.alert
    alert.dismiss()  # or alert.accept()
except NoAlertPresentException:
    logging.info("No alert found")

if total_prods == len(rows):
    logging.info("Test Case Passed: On Dismiss Delete, Products quantity did not decrease")
else:
    logging.error("Test Case Failed: Product quantity decreased on unsuccessful delete")


delete_btn.click()
# Dismiss the alert if present
try:
    alert = driver.switch_to.alert
    alert.accept()  # or alert.accept()
except NoAlertPresentException:
    logging.info("No alert found")

if total_prods == len(rows):
    logging.info("Test Case Passed: On Successful Delete, Products quantity decreased")
else:
    logging.error("Test Case Failed: Product quantity did not decrease on successful delete")

time.sleep(1)
driver.quit()
