#-*- coding: utf-8-*-
import unittest
from selenium import webdriver
import time
import test_data

class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://wizzair.com/pl-pl/')
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()
        pass

    def test_wrong_email(self):
        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath('//button[text()="Rejestracja"]')
        rejestracja_btn.click()
        time.sleep(5)
        name_field = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        name_field.send_keys(test_data.valid_name)
        surname_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys(test_data.valid_surname)

        if test_data.sex =='female':
                gender_switch=driver.find-find_element_by_xpath('//label[@for="register-gender-male"]')
                driver.execute_script("arguments[0].click()", gender_switch)
        else:
                gender_switch= driver.find_element_by_xpath('//label[@for="register-gender-female"]')
                driver.execute_script("arguments[0].click()", gender_switch)
            telphone_field = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
            telphone_field = send.keys(test_data.valid_telephone)
            email_field = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
            email_field = send.keys(test_data.wrong_email)
            password_field = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
            password_field = send.keys(test_data.valid_password)
            country_field=driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
            country_field.click()
            country_to_choose=driver.find_element_by_name('//*[@id="regmodal-scroll-hook-6"]/div[1]/label/label')
            country_to_choose.location_once_scrolled_into_view
            country_to_choose.click()
            privacy_policy=driver.find_element_by_xpath()


            assert error_notice.in.display()
            self.assertEqual(error_notice.get_atribute('inerText'), u"Niebrawodlowy adres email")
            driver.save_screenshot(koniec.pgn)








    def test_search(self):
        pass
        #driver = self.driver
        #driver.get('http://www.google.pl')
        #input = driver.find_element_by_name("q")
        #input.send_keys('tester wsb katowice')
        #sleep(3)


if __name__ == '__main__':
    unittest.main()
