from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
USERNAME = 'accountsic@mailinator.com'  # Replace with your username
PASSWORD = 'Admin@1234'  # Replace with your password
DASHBOARD_SETTINGS_URL = "http://167.71.235.184/dashboard/settings"  # Settings URL


def initialize_driver():
    """Initialize the Chrome WebDriver."""
    driver = webdriver.Chrome()  # Adjust if necessary
    return driver


def login(driver, username, password):
    """Log into the application using provided username and password."""
    driver.get(LOGIN_URL)

    # Find the username and password fields
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))

    # Enter the credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)  # Wait for login to complete


def navigate_to_settings(driver):
    """Navigate to the settings page."""
    driver.get(DASHBOARD_SETTINGS_URL)
    time.sleep(2)  # Wait for the page to load


def click_working_country(driver):
    """Locate and click the 'Working Country' element."""
    working_country_element = driver.find_element(By.XPATH, "//span[text()='Working Country']")
    working_country_element.click()
    time.sleep(2)  # Allow time for the action to complete


def add_working_country(driver):
        """ Locate and click on add button """
        add_button = driver.find_element(By.CSS_SELECTOR, "svg[data-testid='AddIcon']")
        add_button.click()
        time.sleep(2)

def select_dropdown_country(driver):
    """ Select the country from the dropdown"""
    dropdown_arrow=driver.find_element(By.CSS_SELECTOR,"svg[data-testid='ArrowDropDownIcon']")
    dropdown_arrow.click()
    time.sleep(2)
    """ Select country and send the values of country """
    country_name=driver.find_element(By.ID,'country-select-demo')
    country_value="Australia"
    country_name.send_keys(country_value)
    time.sleep(2)
    dropdown_arrow.click()
    time.sleep(2)



def save_button(driver):
    """Click the save button."""
    # Using XPath
    save_button= driver.find_element(By.CSS_SELECTOR, "button.MuiButton-contained.MuiButton-containedPrimary")
    save_button.click()
    time.sleep(2)

    # Check for a success or failure message
    try:
        driver.find_element(By.CSS_SELECTOR, "button.MuiButton-contained.MuiButton-containedPrimary")
        print(f"Success: Country has been added successfully!")
    except:
        # Check if the country already exists
        try:
            driver.find_element(By.CSS_SELECTOR, "button.MuiButton-contained.MuiButton-containedPrimary")
            print(f"Failure:  Country already exists.")
        except:
            print("Failure: An unexpected error occurred while adding the country.")


def main():
    """Main function to execute the script."""
    driver = initialize_driver()
    try:
        login(driver, USERNAME, PASSWORD)
        navigate_to_settings(driver)
        click_working_country(driver)
        add_working_country(driver)
        select_dropdown_country(driver)
        save_button(driver)
    finally:
        driver.quit()  # Ensure the driver is closed


if __name__ == "__main__":
    main()