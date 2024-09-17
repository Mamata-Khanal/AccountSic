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
    onboarding_url=("http://167.71.235.184/dashboard/employee/list/onboarding")
    driver.get(onboarding_url)
    time.sleep(2)

    # click on fiter button
    filter_button = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/div[3]/div[1]/div/span/div/div[1]/div/div[2]/button')
    filter_button.click()
    time.sleep(2)

    # Enter the full name and email
    full_name='Prashant Rawal'
    email="test@mailinator.com"

    # Locate the full name input field and enter the full name
    full_name_input=driver.find_element(By.NAME,'fullName')
    full_name_input.clear()
    full_name_input.send_keys(full_name)

    #Locate the email and enter the email address
    email_input=driver.find_element(By.NAME,'email')
    email_input.clear()
    email_input.send_keys(email)

    # Locate and click the search filter button
    apply_filter=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/div[3]/div[1]/div/span/div/div[2]/div/div/div/div/form/div[2]/button')
    apply_filter.click()
    time.sleep(2)

    #Gather results
    results=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/div[3]/div[1]/div/span/div/div[2]/div/div/div/div/form/div[2]/button')

    # check if results were found
    if results:
        print("result found")
        for result in results:
            print(result.text)
        else:
            print("Empty Result: No matches for full Name: '{}' and Email:'{}'".format(full_name,email))

        # click on reset icon
        reset_button=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/div[3]/div[1]/div/span/div/div[1]/div/div[1]/button')
        reset_button.click()
    time.sleep(2)
except Exception as e:
    print("An error occured:",e)

finally:
    driver.quit()