import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import HtmlTestRunner
logging.basicConfig(level=logging.INFO)
from CommonUtils import CommonUtils
from AdminLoginPage import AdminLoginPage
from UserLoginPage import UserLoginPage
from UserSignupPage import UserSignupPage
from ResetPswdPage import ResetPswdPage
from ForgotPswdPage import ForgotPswdPage
from GetProdsPage import GetProdsPage
from AddProdsPage import AddProdsPage
from EditProdsPage import EditProdsPage
from DeleteProdsPage import DeleteProdsPage

class TestCases(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
    
    def run_navigation_tests(self, page):
        print("<br>Running Tests for Navigation Links.<br>")
        for xpath, expected_url in page.xPaths_Link:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            CommonUtils.navigation_test_status(self.driver, expected_url)
    
    def run_tests(self, page_obj, data_file):
        page = page_obj(self.driver)
        logging.info(f"Running Test Cases For: {page}")
        page.open()

        if (page_obj == EditProdsPage):
            page.click_edit_btn()

        if (page_obj==AddProdsPage):
            page.click_add_btn()
        
        with open(data_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(';')
                toast_message = page.test_form_submission(*data)
                CommonUtils.check_toast_message(lines.index(line) + 1, page.error_messages[lines.index(line)], toast_message)

        if ((page_obj == UserLoginPage) or (page_obj==UserSignupPage) or (page_obj==ResetPswdPage) or (page_obj==ForgotPswdPage)):
            self.run_navigation_tests(page)
    
    def run_get_prods_test(self, page_obj):
        page = page_obj(self.driver)
        logging.info(f"Running Test Cases For: {page}")
        page.open()
        page.test_table_rows_exist()
        page.test_expected_rows_received()
        page.test_expected_data_records()
    
    def run_delete_prods_test(self, page_obj):
        page = page_obj(self.driver)
        logging.info(f"Running Test Cases For: {page}")
        page.open()
        page.test_delete_product()

    # Implement admin login test case
    def test_admin_login(self):
        self.run_tests(AdminLoginPage, './TestDataFiles/testAdminLoginData.txt')
    
    # # Implement user login test case
    def test_user_login(self):
        file_path = './TestDataFiles/testLoginData.txt'
        self.run_tests(UserLoginPage, file_path)
        logging.info(f"Attempting to access file at: {file_path}")

    
    # Implement user signup test case
    def test_user_signup(self):
        self.run_tests(UserSignupPage, './TestDataFiles/testSignupData.txt')
        
    # Implement reset password test case
    def test_reset_pswd(self):
        self.run_tests(ResetPswdPage, './TestDataFiles/testResetPswdData.txt')

    # Implement forgot password test case
    def test_forgot_pswd(self):
        self.run_tests(ForgotPswdPage, './TestDataFiles/testForgotPswdData.txt')
        
    # Implement get products test case
    def test_get_prods(self):
        self.run_get_prods_test(GetProdsPage)
        
    # Implement add products test case
    def test_add_prods(self):
        self.run_tests(AddProdsPage, './TestDataFiles/testAddProdData.txt')
        
    # Implement edit products test case
    def test_edit_prods(self):
        self.run_tests(EditProdsPage, './TestDataFiles/testEditProdData.txt')
        
    # Implement delete products test case
    def test_delete_prods(self):
        self.run_delete_prods_test(DeleteProdsPage)
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))

