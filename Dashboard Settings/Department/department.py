from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
USERNAME = 'accountsic@mailinator.com'  # Replace with your username
PASSWORD = 'Admin@1234'  # Replace with your password

# Initialize the WebDriver
driver = webdriver.Chrome()  # Adjust if necessary
driver.get("http://167.71.235.184/login")
# driver.maximize_window()

try:
    # Find the username and password fields by their name attribute
    username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
    password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))
    # Enter the username and password

    username_field.send_keys("accountsic@mailinator.com")
    password_field.send_keys("Admin@1234")

    # Find the login button by its class name and click it
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)

    # Click setting from dashboard
    settings_url="http://167.71.235.184/dashboard/settings"
    driver.get(settings_url)
    time.sleep(2)

finally:
    driver.quit()

