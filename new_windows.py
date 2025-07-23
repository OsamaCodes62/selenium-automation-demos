from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

chrome_path = r"chrome-win64/chrome.exe"

options = Options()
options.binary_location = chrome_path
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")

driver = uc.Chrome(options=options, use_subprocess= True)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

current_Window = driver.current_window_handle
print("Current window handle :: ", current_Window)

change_Window = driver.window_handles[1]
print("Current window handle :: ", change_Window)
driver.switch_to.window(change_Window)
time.sleep(5)

# driver.close()
driver.switch_to.window(current_Window)

time.sleep(5)
driver.quit()