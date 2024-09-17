from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"
USERNAME = 'accountsic@mailinator.com'
PASSWORD = 'Admin@1234'


def login(driver):
    """Log in to the application."""
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
        login_button = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
        login_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_changes(LOGIN_URL)
        )
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()


def navigate_to_employee_list(driver):
    """Navigate to the employee list page."""
    try:
        # Locate and click the dropdown to show the employee list
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/nav/div/div/div[2]/ul[2]/div'))
        )
        dropdown.click()

        # Wait for dropdown options to be displayed
        time.sleep(1)
    except Exception as e:
        print(f"Failed to navigate to employee list: {e}")
        driver.quit()


def click_all_links(driver):
    """Click on all links and return to the previous page."""
    try:
        # Get all the links on the page
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        # Iterate over each link
        for link in links:
            href = link.get_attribute("href")
            print(f"Clicking on link: {href}")
            link.click()
            time.sleep(2)  # Wait for the page to load
            driver.back()  # Go back to the previous page
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
            )  # Refetch all link elements
    except Exception as e:
        print(f"Error occurred while clicking links: {e}")
    finally:
        driver.quit()


def main():
    """Main function to execute the script."""
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Adjust if necessary

    try:
        login(driver)
        navigate_to_employee_list(driver)
        click_all_links(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

