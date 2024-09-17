from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self,driver):
        self.driver=driver

# Define the login function
def login_to_website(driver, login_url, username, password):
    """
    Logs into a website using the provided credentials.

    :param driver: WebDriver instance
    :param login_url: URL of the login page
    :param username: Username for login
    :param password: Password for login
    """




    # Open the login page
    driver.get(login_url)
    driver.maximize_window()

    try:
        # Locate username and password fields
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password'))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'outlined-adornment-password'))
        )

        # Enter the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Locate and click the login button
        login_button = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
        login_button.click()

        # Optional: Wait for some time to ensure the login completes
        time.sleep(5)

        print("Login successful.")

    except Exception as e:
        print(f"An error occurred during login: {e}")


# Example usage
if __name__ == "__main__":
    # Define your login credentials and URLs
    LOGIN_URL = "http://167.71.235.184/login"
    USERNAME = 'accountsic@mailinator.com'
    PASSWORD = 'Admin@1234'

    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Adjust if necessary

    # Call the login function
    login_to_website(driver, LOGIN_URL, USERNAME, PASSWORD)

    # Optionally, continue with further automation or close the browser
    driver.quit()
