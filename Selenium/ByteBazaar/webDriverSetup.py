from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # Enable headless mode
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

