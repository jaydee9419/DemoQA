from pageObjects.ElementPage import ElementPage
from pageObjects.RadiobuttonPage import RadiobuttonsPage
from utilities.readProperties import ReadConfig
import time

class Test_Radiobutton():
    url = ReadConfig.getApplicationURL()

    def test_radiobutton(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.ep = ElementPage(self.driver)
        self.ep.clickRadioButton()
        time.sleep(2)

        self.rbp = RadiobuttonsPage(self.driver)

        self.rbp.clickYes()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())
        self.rbp.clickImpressive()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())

        self.rbp.clickYes()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())
        self.rbp.clickImpressive()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())

        self.rbp.clickYes()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())
        self.rbp.clickImpressive()
        time.sleep(1)
        print(self.rbp.getSelectedItemInfo())



