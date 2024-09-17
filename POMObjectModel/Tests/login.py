from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from POMObjectModel.Pages.loginPage import loginPage
from POMObjectModel.Pages.dashboardProfile import dashboardProfile

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome() # Instantiate the chrome webdriver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("http://167.71.235.184/login")

        login = loginPage(driver)
        login.enter_username("accountsic@mailinator.com")
        login.enter_password("Admin@1234")
        login.click_login()
        time.sleep(2)

        # self.driver.find_element(By.ID,'outlined-adornment-confirm-password').send_keys("accountsic@mailinator.com")
        # self.driver.find_element(By.ID, 'outlined-adornment-password').send_keys("Admin@1234")
        # self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button').click()
        # time.sleep(2)

        dashboard=dashboardProfile(driver)
        dashboard.click_Profile()
        dashboard.profile_icon()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close() # Close the browser window
        cls.driver.quit()  # Quit the webdriver session
        print("Test completed")

if __name__ == "__main__":
    unittest.main()










