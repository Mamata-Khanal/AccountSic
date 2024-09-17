
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class loginPage():

    def __init__(self,driver):
        self.driver=driver

        self.username_field_ID="outlined-adornment-confirm-password"
        self.password_field_ID="outlined-adornment-password"
        self.login_button_XPATH='//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button'

    def enter_username(self,USERNAME):
        self.driver.find_element(By.ID,self.username_field_ID).clear()
        self.driver.find_element(By.ID, self.username_field_ID).send_keys(USERNAME)

    def enter_password(self, PASSWORD):
            self.driver.find_element(By.ID, self.password_field_ID).clear()
            self.driver.find_element(By.ID, self.password_field_ID).send_keys(PASSWORD)

    def click_login (self):
        self.driver.find_element(By.XPATH,self.login_button_XPATH).click()



