
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
USERNAME = 'accountsic@mailinator.com'  # Replace with your username
PASSWORD = 'Admin@1234'  # Replace with your password


def login_to_website(driver, login_url, username, password):
    """
    Function to log in to the website using the provided credentials.

    Parameters:
    - driver: The WebDriver instance.
    - login_url: The URL of the login page.
    - username: The username for login.
    - password: The password for login.
    """
    driver.get(login_url)
    driver.maximize_window()

    # Wait for the username and password fields to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))

    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Find the login button by its XPath and click it
    login_button = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)


def change_password(driver, old_password, new_password, confirm_password):
    """
    Function to navigate to the profile and change the password.

    Parameters:
    - driver: The WebDriver instance.
    - old_password: The current password.
    - new_password: The new password.
    - confirm_password: The confirmation of the new password.
    """
    # Go to profile
    profile_button = driver.find_element(By.XPATH, '/html/body/div/div/div/header/div/div[8]')
    profile_button.click()
    time.sleep(2)

    # Click on profile icon
    profile_icon = driver.find_element(By.XPATH,
                                       '//div[@class="MuiListItemText-root css-sqh3xd"]/span[contains(@class, "MuiTypography-root")]//p[text()="Profile"]')
    profile_icon.click()
    time.sleep(2)

    # Locate the change password tab and click on it
    change_password_tab = driver.find_element(By.CSS_SELECTOR, "a[id='simple-tab-2']")
    change_password_tab.click()
    time.sleep(2)

    # Enter the old and new passwords
    old_password_field = driver.find_element(By.NAME, 'oldPassword')
    old_password_field.send_keys(old_password)

    new_password_field = driver.find_element(By.NAME, 'password')
    new_password_field.send_keys(new_password)

    confirm_password_field = driver.find_element(By.NAME, 'confirmPassword')
    confirm_password_field.send_keys(confirm_password)
    time.sleep(2)

    # Submit the change password form
    change_password_button = driver.find_element(By.XPATH,
                                                 '/html/body/div/div/div/main/div/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/form/div[4]/button')
    change_password_button.click()
    time.sleep(2)


# Main script execution
driver = webdriver.Chrome()

try:
    login_to_website(driver, LOGIN_URL, USERNAME, PASSWORD)
    change_password(driver, "Admin@1234", "Accountsic@123", "Accountsic@123")
finally:
    driver.quit()
