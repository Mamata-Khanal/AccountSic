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

    # Click on add employee to add the employee
    add_employee=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/button')
    add_employee.click()
    time.sleep(2)

    # Add a new Employee using all the credentials
    First_name="John"
    Last_name="Doe"
    Email="john@mailinator.com"
    Working_country="Switzerland"
    User_type="STAFF"
    Role="Manager"
    Probation_period="Six Month"

    #Enter the firstname and click it
    First_name=driver.find_element(By.NAME,'firstName')
    First_name.send_keys("John")

    # Enter the Lastname and click it
    Last_name= driver.find_element(By.NAME, 'lastName')
    Last_name.send_keys("Doe")

    # Enter the Email and click on it
    Email=driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[3]/div/div/input')
    Email.send_keys('john@mailinator.com')
    time.sleep(2)

    # select the dropdown  of working country
    dropdown_arrow = driver.find_element(By.CSS_SELECTOR, '.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.css-14yq2cq[data-testid="ArrowDropDownIcon"]')
    dropdown_arrow.click()
    time.sleep(2)
    """select country and send the values of the country"""
    country_name=driver.find_element(By.CSS_SELECTOR, 'input[aria-autocomplete="list"]')
    country_name.click()
    country_value="Australia"
    country_name.send_keys(country_value)
    time.sleep(2)
    # Select UserType from the dropdown
    user_type_arrow=driver.find_element(By.CLASS_NAME,"MuiSelect-select")
    user_type_arrow.click()
    time.sleep(2)
    # Send the user type value
    user_type=driver.find_element(By.XPATH,"//li[@role='option' and @data-value='STAFF']")
    user_type.click()
    time.sleep(2)

    # Click the role and select the role
    role_arrow=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[6]/div/div/div ")
    role_arrow.click()
    time.sleep(2)
    role_name=driver.find_element(By.CSS_SELECTOR,'.MuiMenuItem-root[data-value="1"]')
    role_name.click()
    time.sleep(2)

    #Click and select the Probation Period
    probabtion_dropdown=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[7]/div/div/div")
    probabtion_dropdown.click()
    time.sleep(2)
    probation_period=driver.find_element(By.XPATH,"//li[@data-value='FOURTY_FIVE_DAYS']")
    probation_period.click()
    time.sleep(2)

    # CLick on submit button
    submit_button=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button")
    submit_button.click()
    time.sleep(2)
finally:
   time.sleep(5)
   driver.quit()