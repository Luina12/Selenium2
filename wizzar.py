#-*- coding: utf-8-*-
import unittest
import test_data
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://wizzair.com/pl-pl/main-page#/*")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()


#I Rejestracja nowego użytkownika używając adresu email - dane niepoprawne (niekompletny email)
    #
    # def test_wrong_email(self):
    #     driver=self.driver
    #     zaloguj_btn=driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
    #     zaloguj_btn.click()
    #     #time.sleep(2)
    #     rejestracja_btn=driver.find_element_by_xpath("//button[text()='Rejestracja']")
    #     rejestracja_btn.click()
    #     #time.sleep(2)
    #     name_field=driver.find_element_by_xpath("//input[@placeholder='Imię']")
    #     name_field.send_keys(test_data.valid_name)
    #     surname_field=driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    #     surname_field.send_keys(test_data.valid_surname)
    #     if test_data.sex=='female':
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-male"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     else:
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-female"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     telephone_field=driver.find_element_by_xpath("//input[@placeholder='Telefon komórkowy']")
    #     telephone_field.send_keys(test_data.valid_phone)
    #     email_field=driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
    #     email_field.send_keys(test_data.wrong_email)
    #     password_field=driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
    #     password_field.send_keys(test_data.valid_password)
    #     country_field=driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
    #     country_field.click()
    #     country_to_choose=driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
    #     country_to_choose.location_once_scrolled_into_view
    #     country_to_choose.click()
    #     privacy_policy=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]')
    #     privacy_policy.click()
    #     register_btn=driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
    #     register_btn.click()
    #     error_notice=driver.find_element_by_xpath("(//span[contains(text(), 'Nieprawidłowy adres e-mail')])[2]")
    #
    #     assert error_notice.is_displayed()
    #     self.assertEqual(error_notice.get_attribute('innerText'), u"Nieprawidłowy adres e-mail")
    #     driver.save_screenshot('koniec.png')
    #
    #     time.sleep(3)


    # def test_wrong_password(self):
    #     driver=self.driver
    #     zaloguj_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
    #     zaloguj_btn.click()
    #     time.sleep(2)
    #     rejestracja_btn=driver.find_element_by_xpath("//button[text()='Rejestracja']")
    #     rejestracja_btn.click()
    #     time.sleep(2)
    #     name_field=driver.find_element_by_xpath("//input[@placeholder='Imię']")
    #     name_field.send_keys(test_data.ivalid_name)
    #     surname_field=driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    #     surname_field.send_keys(test_data.valid_surname)
    #     if test_data.gender=='female':
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-male"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     else:
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-female"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     telephone_field=driver.find_element_by_xpath("//input[@placeholder='Telefon komórkowy']")
    #     telephone_field.send_keys(test_data.valid_phone)
    #     email_field=driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
    #     email_field.send_keys(test_data.wrong_email)
    #     password_field=driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
    #     password_field.send_keys(test_data.valid_password)
    #     country_field=driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
    #     country_field.click()
    #     country_to_choose=driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
    #     country_to_choose.location_once_scrolled_into_view
    #     country_to_choose.click()
    #     privacy_policy=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]')
    #     privacy_policy.click()
    #     register_btn=driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
    #     register_btn.click()
    #     #error_notice=driver.find_element_by_xpath("(//span[contains(text(), 'Nieprawidłowe hasło')])[2]")
    #
    #     visible_error_notices=[]
    #     errors_notices = self.driver.find_elements('//span[@class="rf-input__error__message"]/span')
    #     for error in error_notices:
    #         if error.is_displayed():
    #             visible_error_notices.append(error)
    #
    #     assert len(error_notices) == 1
    #     error_text = errors[0].get_attribute("innerText")
    #     assert errors_text == u"Nieprawidłowa liczba znaków"


        #assert error_notice.is_displayed()
        #self.assertEqual(error_notice.get_attribute('innerText'), u"Hasło musi zawierać co najmniej 7 znaków")
        #driver.save_screenshot('koniec.png')

    def test_valid_registration(self):
        driver = self.driver
        zaloguj_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()
        name_field = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        name_field.send_keys(test_data.valid_name)
        surname_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys(test_data.valid_surname)
        if test_data.valid_gender == 'male':
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-male']")
            driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-female']")
            driver.execute_script("arguments[0].click()", gender_switch)
        telephone_field = driver.find_element_by_name("mobilePhone")
        telephone_field.send_keys(test_data.valid_phone)
        email_field =  driver.find_element_by_css_selector("input[placeholder='E-mail'][data-test='booking-register-email']")
        email_field.send_keys(test_data.valid_email)
        password_field = driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.valid_password)
        country_field = driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        country_field.click()
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_xpath("label")
        print(test_data.valid_country)
        for label in countries:
            option=label.find_element_by_tag_name('strong')
            # print(d.text)
            if option.get_attribute("innerText") == test_data.valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        privacy_policy = driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox']")
        privacy_policy.click()
        register_btn = driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        assert register_btn.is_enabled()
        error_notices = driver.find_elements_by_xpath('//*[@class="rf-input__error__message"]/span')
        for error in error_notices:
            assert not error.is_displayed()

if __name__ == '__main__':
    unittest.main()
