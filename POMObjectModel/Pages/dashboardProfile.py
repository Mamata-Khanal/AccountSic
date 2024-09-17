from selenium.webdriver.common.by import By


class dashboardProfile():
    def __init__(self,driver):
        self.driver=driver

        self.profile_link_XPATH=" /html/body/div/div/div/header/div/div[8]"
        self.profile_icon_XPATH='//div[@class="MuiListItemText-root css-sqh3xd"]/span[contains(@class, "MuiTypography-root")]//p[text()="Profile"]'
        self.Logout_link_XPATH="Logout"

    def click_Profile(self):
        self.driver.find_element(By.XPATH, self.profile_link_XPATH).click()

    def profile_icon(self):
        self.driver.find_element(By.XPATH, self.profile_icon_XPATH).click()


