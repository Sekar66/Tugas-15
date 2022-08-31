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
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha12") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("haha@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("hahahihi") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_b_fail_registration_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha12") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("haha@gmail") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("hahahihi") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_c_fail_registration_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("mango") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("mangogo") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_d_fail_registration_empty_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("mango") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("mango@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_e_fail_registration_max_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("mangoangoangoangoangoangoangoangoango") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("mango@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("mangogo") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_f_fail_registration_empty_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("mango") # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys("mango@gmail.com") # email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys("") # password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol sign in
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()