# -*-coding: utf-8-*-
import unittest
import time
#from selenium.webdriver.support.ui import Select
#Tworze klase wsbPlCheck dziedziczaca po klasie TestCase z modulu unittest
class WsbPLCheck(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        #sprawdzam czy "wpiszę Szkoły Bankowe znajdują znajduja sie w tytule strony
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)
        print(driver.title)
        time.sleep(3)

    def test_wsb_pl2(self):
        driver = self.driver
        driver.get('http://www.wsb.pl')
        driver.find_element_by_partial_link_text("Studia I stopnia").click()
        time.sleep(5)


    def test_select(self):
        driver = self.driver
        driver.get('http://www.wsb.pl')
        driver.find_element_by_id("edit-city")
        time.sleep(5)
#zamiana
    #def test_select3(self):
    #    driver = self.driver
    #    driver.get('http://www.wsb.pl')
    #    select_city= Select(driver.find_element_by_id("edit-city"))
    #    act_options={}
    #    self.assertEqual(11, len(select_city.options))
    #    act_options=[]
    #    exp_options=['Wybierz miasto','Chorzów','Katowice','Gdansk','Gdynia','Opole','Szczecin','Warszawa']
    #    for option in select_city.act_options:
    #        act_options.append(option.get_attribute("text"))
    #    self.assertEqual(act_option,exp_options)
    #    time.sleep(5)
#wejdz na strone wizzar
#kliknij zaloguj
#kliknij w zarejestruj sie
#podaj imie i nazwisko
#wybierz plec
#podaj nr telefonu
#podaj bledy mail
#wybierz kraj
#akceptuj polityke prywatnosci
#akceptuj newslatter
#klimay zare4jstruj bawimy_sie
#oczekiwany rezultat bledny mail
if __name__ == '__main__':
    unittest.main(verbosity=2)
