from selenium.webdriver.common.by import By


class RadiobuttonsPage():

    radiobutton_yes_xpath = "//label[normalize-space()='Yes']"
    radiobutton_impressive_xpath = "//label[normalize-space()='Impressive']"
    txt_selected_option_xpath = "//div//p"

    def __init__(self, driver):
        self.driver = driver

    def clickYes(self):
        element = self.driver.find_element(By.XPATH, self.radiobutton_yes_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def clickImpressive(self):
        element = self.driver.find_element(By.XPATH, self.radiobutton_impressive_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def getSelectedItemInfo(self):
        msg = self.driver.find_element(By.XPATH, self.txt_selected_option_xpath).text
        return msg
