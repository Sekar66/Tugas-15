import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("hahahihi") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)


    def test_b_failed_login_by_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("hehehe") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_c_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("hhttp://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys(" ") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_d_failed_login_with_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha@gmail") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("hahahihi") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_e_failed_login_with_max_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("haha@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("hahahihihahahihihahahihihahahihi") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

    def test_f_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("hahahihi") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()


