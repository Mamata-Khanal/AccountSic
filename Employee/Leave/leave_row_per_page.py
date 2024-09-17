from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your login credentials and URLs
LOGIN_URL = "http://167.71.235.184/login"  # Replace with the actual login URL
USERNAME = 'accountsic@mailinator.com'  # Replace with your username
PASSWORD = 'Admin@1234'  # Replace with your password

# Initialize the WebDriver
driver = webdriver.Chrome()  # Adjust if necessary
driver.get("http://167.71.235.184/login")
try:
    # Find the username and password fields by their name attribute
    username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'outlined-adornment-confirm-password')))
    password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'outlined-adornment-password')))
    # Enter the username and password

    username_field.send_keys("accountsic@mailinator.com")
    password_field.send_keys("Admin@1234")

    # Find the login button by its class name and click it
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button')
    login_button.click()
    time.sleep(5)

    #Navigate to the URL
    leave_url=("http://167.71.235.184/dashboard/employee/list/leave")
    driver.get(leave_url)
    time.sleep(2)

    # Select the row per page
    # Define the options you want to test
    options_to_test = ['5', '10', '25', 'All']

    # XPath for the dropdown element
    dropdown_xpath = "//select[@class='base-TablePagination-select']"

    # Loop through each option in the list and select it
    for option in options_to_test:
        # Locate the "Rows per page" dropdown and select the option
        rows_per_page_dropdown = Select(driver.find_element(By.XPATH, dropdown_xpath))

        if option == "All":
            rows_per_page_dropdown.select_by_visible_text(option)
        else:
            rows_per_page_dropdown.select_by_value(option)

        # Wait for a short period to observe the change
        time.sleep(2)
        print(f"Selected rows per page: {option}")
finally:
    driver.quit()


