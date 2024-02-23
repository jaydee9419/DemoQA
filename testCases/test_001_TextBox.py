from pageObjects.ElementPage import ElementPage
from pageObjects.TextBoxPage import TextBoxPage
from utilities.readProperties import ReadConfig
import time

class Test_TextBox():
    url = ReadConfig.getApplicationURL()

    def test_textbox(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.ep = ElementPage(self.driver)
        self.ep.clickTextBox()

        self.tbp = TextBoxPage(self.driver)
        self.tbp.setUsername("ABC")
        self.tbp.setMail("abc@gamil.com")
        self.tbp.setCurrentAddress("Vijayawada")
        self.tbp.setPermanentAddress("Bangalore")
        print("Details entered")
        self.tbp.clickSubmit()
        print("Button clicked")
        time.sleep(3)
        details = self.tbp.getUserDetails()
        for item in details:
            print(item)
        time.sleep(3)
        self.driver.quit()
