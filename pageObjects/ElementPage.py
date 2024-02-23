from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ElementPage():
    span_textbox_xpath = "//span[normalize-space()='Text Box']"
    span_checkbox_xpath = "//span[normalize-space()='Check Box']"
    span_radiobutton_xpath = "//span[normalize-space()='Radio Button']"
    span_web_tables_xpath = "//span[normalize-space()='Web Tables']"
    span_buttons_xpath = "//span[normalize-space()='Buttons']"
    span_links_xpath = "//span[normalize-space()='Links']"
    span_broken_link_img_xpath = "//span[normalize-space()='Broken Links - Images']"
    span_upload_download_xpath = "//span[normalize-space()='Upload and Download']"
    span_dynamic_properties_xpath = "//span[normalize-space()='Dynamic Properties']"


    def __init__(self, driver):
        self.driver = driver

    def clickTextBox(self):
        self.driver.find_element(By.XPATH, self.span_textbox_xpath).click()

    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.span_checkbox_xpath).click()

    def clickRadioButton(self):
        self.driver.find_element(By.XPATH, self.span_radiobutton_xpath).click()

    def clickWebTable(self):
        self.driver.find_element(By.XPATH, self.span_web_tables_xpath).click()

    def clickButtons(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.span_buttons_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        self.driver.find_element(By.XPATH, self.span_buttons_xpath).click()

    def clickLinks(self):
        self.driver.find_element(By.XPATH, self.span_links_xpath).click()

    def clickBrokenLinksAndImages(self):
        self.driver.find_element(By.XPATH, self.span_broken_link_img_xpath).click()

    def clickUploadAndDownload(self):
        self.driver.find_element(By.XPATH, self.span_upload_download_xpath).click()

    def clickDynamicProperties(self):
        self.driver.find_element(By.XPATH, self.span_dynamic_properties_xpath).click()

