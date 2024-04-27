# from webDriverSetup import get_chrome_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging

# logging.basicConfig(level=logging.INFO)

# driver = get_chrome_driver()
# driver.get('http://localhost:5173/bytebazaar/admin/manage-inventory')

# print("Title: ", driver.title)

# # Locate the table by tag name 'table'
# table = driver.find_element(By.TAG_NAME, 'table')

# exp_rows = 5

# # Find all rows (<tr>) within the table's tbody
# rows = table.find_elements(By.XPATH, "./tbody/tr")

# displayed_rows = len(rows)
# logging.info(displayed_rows)

# if exp_rows == displayed_rows:
#     logging.info("Test Case Passed: No of Expected Records in a Table Received.")
# else:
#     logging.error("Test Case Failed: Expected Data Records not Received.")

# for i in range(displayed_rows):
#     txt = rows[i].text

#     if (txt!="No Products Found"):
#         displayed_records = txt.split("\n")
#         num_records= len(displayed_records)
#         if(num_records==6):
#             logging.info(f"Test Case Passed: No of Expected Data Rows Received for ${displayed_records[0]}")
#         else:
#             logging.error(f"Test Case Failed: Expected Data Rows not Received for ${displayed_records[0]}")
#     else:
#         logging.error(f"Test Case Failed: No Products Found.")

# time.sleep(1)
# driver.quit()

import unittest
from webDriverSetup import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class TestTableVerification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.driver.get('http://localhost:5173/bytebazaar/admin/manage-inventory')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_table_rows_exist(self):
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        self.assertTrue(len(rows) > 0, "No rows found in the table")

    def test_expected_rows_received(self):
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        expected_rows = 5
        self.assertEqual(len(rows), expected_rows, f"Expected {expected_rows} rows, received {len(rows)}")

    def test_expected_data_records(self):
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        for row in rows:
            txt = row.text
            if txt != "No Products Found":
                displayed_records = txt.split("\n")
                num_records = len(displayed_records)
                self.assertEqual(num_records, 6, f"Expected 6 data records, received {num_records} for {displayed_records[0]}")

if __name__ == '__main__':
    unittest.main()
