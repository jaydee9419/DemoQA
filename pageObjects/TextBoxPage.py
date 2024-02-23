from selenium.webdriver.common.by import By


class TextBoxPage():
    input_name_xpath = "//input[@id='userName']"
    input_mail_xpath = "//input[@id='userEmail']"
    input_current_address_xpath = "//textarea[@id='currentAddress']"
    input_permanent_address_xpath = "//textarea[@id='permanentAddress']"
    btn_submit_xpath = "//button[@id='submit']"
    text_output_xpath = "//div//p"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, uname):
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(uname)

    def setMail(self, mail):
        self.driver.find_element(By.XPATH, self.input_mail_xpath).send_keys(mail)

    def setCurrentAddress(self, c_add):
        self.driver.find_element(By.XPATH, self.input_current_address_xpath).send_keys(c_add)

    def setPermanentAddress(self, p_add):
        self.driver.find_element(By.XPATH, self.input_permanent_address_xpath).send_keys(p_add)

    def clickSubmit(self):
        element = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def getUserDetails(self):
        try:
            details = self.driver.find_elements(By.XPATH, self.text_output_xpath)
            return details

        except:
            print("Unable to get the user details")
