from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    lnk_element_xpath = "div[class='category-cards'] div:nth-child(1) div:nth-child(1) div:nth-child(2)"
    lnk_forms_xpath = "//div[@class='category-cards']//div[2]//div[1]//div[2]//*[name()='svg']"
    lnk_alert_frame_windows_xpath = "//div[@class='category-cards']//div[3]//div[1]//div[2]//*[name()='svg']"
    lnk_widgets_xpath = "//div[@class='category-cards']//div[4]//div[1]//div[2]//*[name()='svg']"
    lnk_interactions_xpath = "//div[@class='category-cards']//div[5]//div[1]//div[2]//*[name()='svg']"
    lnk_bookstore_xpath = "//div[@class='category-cards']//div[6]//div[1]//div[2]//*[name()='svg']"


    def __init__(self, driver):
        self.driver = driver

    def clickElement(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.lnk_element_xpath))
        )
        element.click()
        # self.driver.find_element(By.XPATH, self.lnk_element_xpath).click()

    def clickForms(self):
        self.driver.find_element(By.XPATH, self.lnk_forms_xpath).click()

    def clickAletrsFramesWindows(self):
        self.driver.find_element(By.XPATH, self.lnk_alert_frame_windows_xpath).click()

    def clickWidgets(self):
        self.driver.find_element(By.XPATH, self.lnk_widgets_xpath).click()

    def clickInteractions(self):
        self.driver.find_element(By.XPATH, self.lnk_interactions_xpath).click()

    def clickBookStore(self):
        self.driver.find_element(By.XPATH, self.lnk_bookstore_xpath).click()

