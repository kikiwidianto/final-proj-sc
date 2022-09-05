import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_time_valid(self): #Searching For Valid Data
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu Time
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("charlie")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div[2]/div/span").click() 
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click() #button view
        time.sleep(2)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/h6").text
        self.assertTrue('Timesheet for', text_atas)
    
    def test_b_time_invalid(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(4)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(4)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() #menu time
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("lalala")
        time.sleep(4)     
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div[2]/div").click() 
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click() #button view
        time.sleep(2)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/span").text
        
        self.assertIn('Time', text_atas)
        self.assertTrue(text_bawah, 'Required')

    def test_c_time_nodata(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu Time
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click() #klik tombol view
        time.sleep(5)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/span").text
        
        self.assertIn('Time', text_atas)
        self.assertEqual(text_bawah, 'Required')
            
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()