import unittest
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.binary_location = r"chrome-win64/chrome.exe"
options.add_argument("--no-sandbox")  


class SwagLabTestCaase(unittest.TestCase):
    def setUp(self):
        self.driver = uc.Chrome(options= options)
        self.driver.get("https://www.saucedemo.com/v1")

    def test_login(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
        str = self.driver.find_element(By.XPATH, "//div[@class = 'product_label']").texts

        self.assertEqual("Products", str)
        print("Test passed successfully")


    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()