import pytest
from PageObjects.HomePage import HomePage
from Utilities.Dataclass import Baseclass
from TestData.HomePagedata import Homepagedata


@pytest.mark.usefixtures("setup")
class Testcases(Baseclass):

    def test_Testcases1(self, getData):
        log = self.get_logger()
        Searchbar = HomePage(self.driver)
        Searchbar.Enter_searchbar().send_keys(getData["Productname"])
        log.info("Text entered " + getData["Productname"])
        Searchbar.Click_searchbutton().click()
        log.info("Clicked on search button'")
    @pytest.fixture(params=Homepagedata.test_buylaptop_data)
    def getData(self, request):
        return request.param
