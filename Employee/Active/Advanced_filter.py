
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

def active(driver):
    """Navigates to the active button_page"""
    Active_Url="http://167.71.235.184/dashboard/employee/list/active"
    driver.get(Active_Url)
    time.sleep(2)

def filter_icon(driver):
    filter_button=driver.find_element(By.CSS_SELECTOR,'svg[data-testid="FilterAltOutlinedIcon"]')
    filter_button.click()
    time.sleep(2)

    """ click and send values of fullname"""
    full_name="Mamata Khanal"
    fullname_button=driver.find_element(By.NAME,'fullName')
    fullname_button.click()
    time.sleep(2)
    fullname_button.send_keys(full_name)
    time.sleep(2)

    """ Click and send values of Email """
    email="mamata@mailinator.com"
    email_button=driver.find_element(By.NAME,'email')
    email_button.click()
    time.sleep(2)
    email_button.send_keys(email)
    time.sleep(2)

def Apply_filter(driver):
    apply_filter_button=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/div[2]/div[1]/div/span/div/div[2]/div/div/div/div/form/div[2]/button')
    apply_filter_button.click()
    time.sleep(2)


def main():
    """Main function to execute the script."""
    driver = initialize_driver()

    try:
        login(driver, USERNAME, PASSWORD)
        active(driver)
        filter_icon(driver)
        Apply_filter(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()