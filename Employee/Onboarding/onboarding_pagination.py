from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"
USERNAME = 'accountsic@mailinator.com'
PASSWORD = 'Admin@1234'
ONBOARDING_URL = "http://167.71.235.184/dashboard/employee/list/onboarding"

def login(driver):
    """Login to the application."""
    driver.get(LOGIN_URL)
    try:
        # Find username and password fields
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password'))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'outlined-adornment-password'))
        )

        # Enter username and password
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)

        # Find and click the login button
        login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
        login_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_changes(LOGIN_URL)
        )
    except Exception as e:
        print("Login failed:", e)
        driver.quit()

def navigate_to_onboarding(driver):
    """Navigate to the onboarding employee list page."""
    driver.get(ONBOARDING_URL)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(ONBOARDING_URL)
    )

def pagination_test(driver):
    """Test pagination functionality."""
    try:
        # Next button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[3]/table/tfoot/tr/td/div/div[2]/button[3]'))
        )
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages to navigate.")
        else:
            next_button.click()
            time.sleep(2)

            # Previous button
            previous_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[3]/table/tfoot/tr/td/div/div[2]/button[2]'))
            )
            previous_button.click()
            time.sleep(2)

            # Last page button
            last_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[3]/table/tfoot/tr/td/div/div[2]/button[4]'))
            )
            last_page.click()
            time.sleep(2)

            # First page button
            first_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/div/div[3]/div[3]/table/tfoot/tr/td/div/div[2]/button[1]'))
            )
            first_page.click()
            time.sleep(2)
    except Exception as e:
        print("Pagination error occurred:", e)

def main():
    """Main function to run the script."""
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        login(driver)
        navigate_to_onboarding(driver)
        pagination_test(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
