#-*- coding: utf-8-*-
from base_page import Basepage

class HomePage(BasePage):
    def verify_page(self):
        assert('Oficjalna strona Wizzar' in self.driver.title)

    def click_zaloguj_button(self):
        btn=self.driver.find_element(*HomePageLocator)
