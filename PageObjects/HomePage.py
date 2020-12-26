from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver
    searchbar = (By.CSS_SELECTOR, "[id='twotabsearchtextbox']")
    searchbutton = (By.CSS_SELECTOR, "[value='Go']")
    def Enter_searchbar(self):
        return self.driver.find_element(*HomePage.searchbar)
    def Click_searchbutton(self):
        return self.driver.find_element(*HomePage.searchbutton)