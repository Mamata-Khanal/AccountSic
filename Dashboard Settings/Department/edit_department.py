from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"
USERNAME = 'accountsic@mailinator.com'
PASSWORD = 'Admin@1234'


def initialize_driver():
    """Initialize the WebDriver and return it."""
    driver = webdriver.Chrome()  # Adjust if necessary
    return driver


def login(driver, username, password):
    """Log in to the application."""
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password'))
    )
    username_field = driver.find_element(By.ID, 'outlined-adornment-confirm-password')
    password_field = driver.find_element(By.ID, 'outlined-adornment-password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)


def navigate_to_settings(driver):
    """Navigate to the settings page."""
    settings_url = "http://167.71.235.184/dashboard/settings"
    driver.get(settings_url)
    time.sleep(2)


def edit_department_name(driver,new_department_name):
    """Edit the department name."""
    edit_button = driver.find_element(By.CSS_SELECTOR, 'svg[data-testid="EditNoteIcon"]')
    edit_button.click()
    time.sleep(2)

    department_name_input = driver.find_element(By.CSS_SELECTOR, '#name')
    department_name_input.click()
    time.sleep(2)

    # Clear the old department name
    driver.execute_script("arguments[0].value = '';", department_name_input)

    # Verify that the input has been cleared
    assert department_name_input.get_attribute('value') == "", "Input field was not cleared successfully."

    # Enter the new department name
    department_name_input.send_keys(new_department_name)

    # Click on confirm button to save changes
    confirm_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[1]')
    confirm_button.click()
    time.sleep(2)


def main():
    """Main function to execute the script."""
    driver = initialize_driver()

    try:
        login(driver, USERNAME, PASSWORD)
        navigate_to_settings(driver)
        edit_department_name(driver, "Subtract")  # Add new department name here

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()



