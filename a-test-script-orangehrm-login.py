import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

# ===== Positif Test Case ====        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        info_a = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        info_b = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertIn('PIM', info_a)
        self.assertEqual(info_b, 'Employee Information')

# ===== Negatif Test Case =====
    def test_b_failed_login_invalid_pass(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("asdjklasdjkl") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        info = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertTrue('Invalid credentials', info)

    def test_c_failed_login_invalid_uname(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("bukan") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)
        
        # validasi
        info = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertTrue('Invalid credentials', info)

    def test_d_failed_login_invalid_uname_pass(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("bukan") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("adminloh") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)
        
        # validasi
        info = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertTrue('Invalid credentials', info)

    def test_e_failed_login_no_data(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)
        
        # validasi
        infouname = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        infopass = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        self.assertTrue('Required', infouname)
        self.assertTrue('Required', infopass)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()