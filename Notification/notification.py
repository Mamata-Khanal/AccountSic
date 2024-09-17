import select

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


#Click the notification
def notification(driver):
    notification_button=driver.find_element(By.XPATH,'/html/body/div/div/div/header/div/div[6]/div')
    notification_button.click()
    time.sleep(2)


# Click all the notifications dropdown
def notification_dropdown(driver):
    dropdown_icon=driver.find_element(By.ID,'outlined-select-currency-native')
    dropdown_icon.click()
    time.sleep(2)

#Create a Select object
    select=Select(dropdown_icon)
    # Iterate through  all options and select each one
    for option in select.options:
        select.select_by_value(option.get_attribute('value'))
        print(f'Selected:{option.text}')
        time.sleep(2)

    mark_as_all_read=driver.find_element(By.TAG_NAME,"a")
    mark_as_all_read.click()
    time.sleep(2)


def main():
    """Main function to execute the script."""
    driver = initialize_driver()

    try:
        login(driver, USERNAME, PASSWORD)
        notification(driver)
        notification_dropdown(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()