# 🧪 Selenium Script Collection

This repository contains multiple standalone Selenium automation scripts for different websites and testing scenarios using Python and `undetected_chromedriver`. Each script demonstrates a specific concept such as element interaction, window handling, and unit test automation.

---

## 📁 Files Overview

```
├── web_element.py         # Automates form inputs and cart interaction on Demo Web Shop  
├── swagLabUnitTest.py     # Login test case for SauceDemo using unittest framework  
├── new_windows.py         # Demonstrates handling of multiple browser windows  
├── requirements.txt       # Required Python packages for all scripts  
```

---

## 🧩 Script Descriptions

### 🔹 `web_element.py`

- Site: https://demowebshop.tricentis.com/
- Automates the following:
  - Navigates to the registration page and fills basic fields
  - Clicks login and toggles "Remember Me"
  - Navigates to "Books", adds a book to the cart
  - Verifies cart count
  - Opens the cart and selects a shipping country

Use Cases:
- Web element interaction via various locator strategies (ID, LINK_TEXT, CSS_SELECTOR, XPATH)
- Select dropdown handling using `Select`
- Basic automation flow with validations

---

### 🔹 `swagLabUnitTest.py`

- Site: https://www.saucedemo.com/v1
- A unit test class using `unittest`
- Automates:
  - Login with `standard_user` credentials
  - Verifies login success by checking the presence of the "Products" label

Use Cases:
- Demonstrates structured testing with `setUp`, `test_login`, and `tearDown`
- Assertion example using `assertEqual`
- Example of test output for CI-friendly logging

Note: There’s a small bug in this script. Change:
```python
str = self.driver.find_element(...).texts
```
to:
```python
str = self.driver.find_element(...).text
```

---

### 🔹 `new_windows.py`

- Site: https://the-internet.herokuapp.com/windows
- Automates:
  - Clicking a link to open a new window
  - Switching between original and new window handles
  - Printing window handle info and switching context back

Use Cases:
- Handling multiple tabs/windows using `driver.window_handles`
- Switching and closing windows
- `WebDriverWait` and delay demonstration

---

## 🧱 Requirements

All dependencies are listed in `requirements.txt`.

Install them using:

```
pip install -r requirements.txt
```

Minimum:
- Python 3.8+
- Google Chrome installed
- Internet access for target URLs

---

## 🚀 How to Run

Each script is standalone. Run any script like this:

```
python script_name.py
```

Example:

```
python web_element.py
```

---

## 📌 Future Plans

✅ Add test reports (e.g., pytest-html, unittest-xml-reporting)  
✅ Include edge/negative login cases  
✅ Add test steps for product/cart/inventory pages  
✅ Integrate CI tools (GitHub Actions, Jenkins)
