from selenium.webdriver.common.by import By



class CheckboxPage():

    box_home_xpath = "//label[@for='tree-node-home']//span[@class='rct-checkbox']//*[name()='svg']"
    txt_selected_items_xpath = "//span[normalize-space()='home']"


    def __init__(self, driver):
        self.driver = driver

    def clickHome(self):
        try:
            element = self.driver.find_element(By.XPATH, self.box_home_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except:
            print("Unable to click the checkbox")
        # self.driver.find_element(By.XPATH, self.box_home_xpath).click()

    def getSelectedItemsResult(self):
        try:
            result = self.driver.find_element(By.XPATH, self.txt_selected_items_xpath)
            return result
        except:
            print("Unable to find the resulted items")
