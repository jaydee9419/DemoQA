from pageObjects.ElementPage import ElementPage
from pageObjects.WebtablePage import WebtablePage
from utilities.readProperties import ReadConfig
import time

class Test_Webtable():
    url = ReadConfig.getApplicationURL()

    def test_webtable(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.ep = ElementPage(self.driver)
        self.ep.clickWebTable()
        time.sleep(2)
        #
        self.wtp = WebtablePage(self.driver)
        data = self.wtp.getTabledata()
        for item in data:
            print("========================================")
            print(item.text)

        time.sleep(3)
        self.driver.quit()
