import unittest
import time
from webbrowser import BaseBrowser
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):  # TEST SCENARIO
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
            
    def test_a_success_registration(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click() # klik button sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("dicttaah") # name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("dicttaah@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("dicttaah") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn('berhasil', text_atas)
        self.assertEqual(text_bawah, 'created user!')

    def test_b_invalid_email_registration(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click() # klik button sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("dictta") # name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("dictta@gmail") # email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("dictta1") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_c_fail_registration_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click() # klik button sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("dictta") # name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("dictta@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_d_fail_registration_with_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click() # klik button sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("dmaya") # name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("dmayagmail.com") # email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("dmaya") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text

        self.assertIn('Please include', text_atas)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()