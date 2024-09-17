from POMObjectModel.Locators import locators




class locators():

    #Login page objects

    username_field_ID = "outlined-adornment-confirm-password"
    password_field_ID = "outlined-adornment-password"
    login_button_XPATH = '//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/button'


    # dashboardPage objects
    profile_link_XPATH = " /html/body/div/div/div/header/div/div[8]"
    profile_icon_XPATH = '//div[@class="MuiListItemText-root css-sqh3xd"]/span[contains(@class, "MuiTypography-root")]//p[text()="Profile"]'
    Logout_link_XPATH = "Logout"