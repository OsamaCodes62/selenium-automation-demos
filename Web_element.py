import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time
options = Options()
options.add_argument("--no-sandbox")
# options.add_experimental_option("detach", True)
options.add_argument("--disable-dev-shm-usage")


options.binary_location = r"chrome-win64/chrome.exe"

driver = uc.Chrome(options= options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "ico-register"))
)
register = driver.find_element(By.LINK_TEXT,"Register")
register.click()
gender = driver.find_element(By.ID, "gender-male")
gender.click()

first_name = driver.find_element(By.ID, "FirstName")
first_name.send_keys("Dummy Text")

Last_name = driver.find_element(By.ID, "LastName")
Last_name.send_keys("Text Dummy")

driver.find_element(By.LINK_TEXT, "Log in").click()
remember_me = driver.find_element(By.XPATH, "//input[@id='RememberMe']")
remember_me.click()

driver.find_element(By.LINK_TEXT, "BOOKS").click()

product = driver.find_element(By.CSS_SELECTOR, "div.product-item[data-productid='13']")
add_to_cart = product.find_element(By.CSS_SELECTOR, ".button-2")
add_to_cart.click()

time.sleep(4)
cart_count = driver.find_element(By.XPATH, "//span[@class='cart-qty']").text.strip("()")
cart_count = int(cart_count)
print(cart_count)

driver.find_element(By.LINK_TEXT, "Shopping cart").click()
select = Select(driver.find_element(By.ID, "CountryId"))
select.select_by_value("35")

input("Press any Key...")
driver.quit()