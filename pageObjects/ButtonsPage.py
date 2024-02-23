from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class ButtonsPage():
    btn_double_click_xpath = "//button[@id='doubleClickBtn']"
    btn_right_click_xpath = "//button[@id='rightClickBtn']"
    btn_single_click_xpath = "//button[normalize-space()='Click Me']"
    txt_after_clicking_xpath = "//div//p"

    def __init__(self, driver):
        self.driver = driver

        self.actions = ActionChains(self.driver)

    def clickDouble(self):
        element = self.driver.find_element(By.XPATH, self.btn_double_click_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.actions.double_click(element).perform()

    def clickRight(self):
        element = self.driver.find_element(By.XPATH, self.btn_right_click_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.actions.context_click(element).perform()


    def clickSingle(self):
        element = self.driver.find_element(By.XPATH, self.btn_single_click_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        element.click()

    def getResults(self):
        element = self.driver.find_elements(By.XPATH, self.txt_after_clicking_xpath)
        return element


