from pageObjects.ElementPage import ElementPage
from pageObjects.ButtonsPage import ButtonsPage
from utilities.readProperties import ReadConfig
import time


class Test_Buttons():
    url = ReadConfig.getApplicationURL()

    def test_buttons(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.ep = ElementPage(self.driver)
        self.ep.clickButtons()
        print("Button clicked")
        time.sleep(1)

        self.bp = ButtonsPage(self.driver)
        self.bp.clickSingle()
        self.bp.clickDouble()
        self.bp.clickRight()

        result = self.bp.getResults()
        for item in result:
            print(item.text)

        self.driver.quit()
