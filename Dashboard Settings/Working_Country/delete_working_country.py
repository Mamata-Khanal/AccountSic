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

def click_working_country(driver):
    """Locate and click the 'Working Country' element."""
    working_country_element = driver.find_element(By.XPATH, "//span[text()='Working Country']")
    working_country_element.click()
    time.sleep(2)  # Allow time for the action to complete


def three_dotted_icon(driver):
    """ Locate and click three dotted icon """
    dotted_icon=driver.find_element(By.CSS_SELECTOR,'svg[data-testid="MoreHorizOutlinedIcon"]')
    dotted_icon.click()
    time.sleep(2)

def click_delete_icon(driver):
    """Locate and click the delete icon."""
    delete_icon= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium"))
    )

    # svg_elements = driver.find_elements(By.TAG_NAME, "svg")
    # for svg in svg_elements:
    #     if 'DeleteOutlineIcon' in svg.get_attribute('data-testid'):
    #         svg.click()
    #         break

    delete_icon.click()
    time.sleep(2)


def main():
    """Main function to execute the script."""
    driver = initialize_driver()
    driver.maximize_window()

    try:
        login(driver, USERNAME, PASSWORD)
        navigate_to_settings(driver)

        click_working_country(driver)
        three_dotted_icon(driver)
        click_delete_icon(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()