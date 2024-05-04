from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonUtils import CommonUtils

class AddProdsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:5173/bytebazaar/admin/manage-inventory'
        self.error_messages = [
            'Product Id must be a positive number.',
            'Product Name must not exceed 30 characters.',
            'Product Description must not exceed 200 characters.',
            'Product Category must not exceed 20 characters.',
            'Product Brand must not exceed 20 characters.',
            'Product Price must be a positive number.',
            'Product Rating must be a positive number.',
            'Product Id already exists.',
            'Product Created Successfully.',
        ]

    def open(self):
        self.driver.get(self.url)

    def click_add_btn(self):
        add_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-prods")))
        add_button.click()

    def test_form_submission(self, id, name, price, image, category, brand, rating, description):
        id_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='id']")
        name_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        price_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='price']")
        image_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='image']")
        category_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='category']")
        brand_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='brand']")
        rating_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='rating']")
        description_input = self.driver.find_element(By.CSS_SELECTOR, "textarea[name='description']")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        CommonUtils.clear_and_send_keys(id_input, id)
        CommonUtils.clear_and_send_keys(name_input, name)
        CommonUtils.clear_and_send_keys(price_input, price)
        CommonUtils.clear_and_send_keys(image_input, image)
        CommonUtils.clear_and_send_keys(category_input, category)
        CommonUtils.clear_and_send_keys(brand_input, brand)
        CommonUtils.clear_and_send_keys(rating_input, rating)
        CommonUtils.clear_and_send_keys(description_input, description)
        
        submit_button.click()

        try:
            return (CommonUtils.handle_toasts(self.driver))
        
        except TimeoutException:
            CommonUtils.page_refresh(self.driver, 9, 'Add Products', submit_button)
