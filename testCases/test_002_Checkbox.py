from pageObjects.ElementPage import ElementPage
from pageObjects.CheckboxPage import CheckboxPage
from utilities.readProperties import ReadConfig
import time

class Test_Checkbox():
    url = ReadConfig.getApplicationURL()

    def test_checkbox(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.ep = ElementPage(self.driver)
        self.ep.clickCheckBox()
        time.sleep(2)

        self.cbp = CheckboxPage(self.driver)
        self.cbp.clickHome()
        time.sleep(1)
        self.cbp.clickHome()
        time.sleep(1)
        self.cbp.clickHome()
        time.sleep(1)
        self.cbp.clickHome()
        time.sleep(1)
        self.cbp.clickHome()
        time.sleep(1)
        self.driver.quit()


