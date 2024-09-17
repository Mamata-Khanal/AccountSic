from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URL
LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
USERNAME = 'accountsic@mailinator.com'  # Replace with your username
PASSWORD = 'Admin@1234'  # Replace with your password

def login(driver):
    """Logs into the application."""
    driver.get(LOGIN_URL)

    # Wait for username and password fields to be visible and enter credentials
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)  # Wait for login process to complete

def go_to_settings(driver):
    """Navigates to the settings page."""
    settings_url = "http://167.71.235.184/dashboard/settings"
    driver.get(settings_url)
    time.sleep(2)  # Wait for the settings page to load

def delete_department(driver, department_name):
    """
    Deletes a department by clicking the delete button and confirming the deletion.

    :param department_name: The name of the department to be deleted.
    """
    try:
        # Wait until the delete button for the specified department is visible and click it
        delete_button = driver.find_element(By.CSS_SELECTOR, 'svg[data-testid="DeleteOutlineIcon"]')
        delete_button.click()
        time.sleep(2)  # Wait for the confirmation dialog to appear

        # Click on the confirm button to delete the department
        confirm_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]')
        confirm_button.click()
        time.sleep(2)  # Wait for the deletion to take effect
        print(f"Department '{department_name}' deleted successfully.")

    except Exception as e:
        print(f"An error occurred during deletion: {str(e)}")

def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Adjust if necessary
    driver.maximize_window()

    try:
        # Perform login
        login(driver)

        # Navigate to settings
        go_to_settings(driver)

        # Delete a specific department
        department_name = "Automates"  # Specify the department name to delete
        delete_department(driver, department_name)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# #
# # Define your login credentials and URLs
# LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
# USERNAME = 'accountsic@mailinator.com'  # Replace with your username
# PASSWORD = 'Admin@1234'  # Replace with your password
#
#     # Initialize the WebDriver
# driver = webdriver.Chrome()  # Adjust if necessary
# driver.get("http://167.71.235.184/login")
# # driver.maximize_window()
#
# try:
#     # Find the username and password fields by their name attribute
#     username_field = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
#     password_field = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))
#     # Enter the username and password
#
#     username_field.send_keys("accountsic@mailinator.com")
#     password_field.send_keys("Admin@1234")
#
#     # Find the login button by its class name and click it
#     login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
#     login_button.click()
#     time.sleep(5)
#
#     # Click setting from dashboard
#     settings_url="http://167.71.235.184/dashboard/settings"
#     driver.get(settings_url)
#     time.sleep(2)
#
#
#
#     # Wait until the department name is visible and click on it
#     department_name="ABC"
#     delete_button=driver.find_element(By.CSS_SELECTOR,'svg[data-testid="DeleteOutlineIcon"]')
#     delete_button.click()
#     time.sleep(2)
#
#     #Click on comfirm button to delete the department
#     confirm_button=driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[3]/button[2]')
#     confirm_button.click()
#     time.sleep(2)
#
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
#
#
# finally:
#     driver.quit()


