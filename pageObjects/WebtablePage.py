from selenium.webdriver.common.by import By


class WebtablePage():
    table_data_xpath = "//div[@class='rt-tr-group'][position() <= 3]"



    def __init__(self, driver):
        self.driver = driver

    def getTabledata(self):
        data = self.driver.find_elements(By.XPATH, self.table_data_xpath)
        return data
