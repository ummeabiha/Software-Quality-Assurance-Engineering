from selenium.webdriver.common.by import By
import time 

class GetProdsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/admin/manage-inventory'

    def open(self):
        self.driver.get(self.url)

    def test_table_rows_exist(self):
        time.sleep(1)
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        if len(rows) > 0:
            print("Test case 1 passed: Rows found in the table. <br>")
        else:
            print("<span style='color: red;'>Test case 1 failed: No rows found in the table.</span><br>")

    def test_expected_rows_received(self):
        time.sleep(1)
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        expected_rows = 2
        if len(rows) == expected_rows:
            print(f"Test case 2 passed: Expected {expected_rows} rows received. <br>")
        else:
            print(f"<span style='color: red;'>Test case 2 failed: Expected {expected_rows} rows, received {len(rows)}.</span><br>")

    def test_expected_data_records(self):
        time.sleep(1)
        table = self.driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.XPATH, "./tbody/tr")
        for row in rows:
            txt = row.text
            if txt != "No Products Found":
                displayed_records = txt.split("\n")
                num_records = len(displayed_records)
                if num_records == 6:
                    print(f"Test case 3 passed: Expected 6 data records received for {displayed_records[0]}. <br>")
                else:
                    print(f"<span style='color: red;'>Test case 3 failed: Expected 6 data records, received {num_records} for {displayed_records[0]}.</span><br>")
