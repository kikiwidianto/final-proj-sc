import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_myinfo_view_detail(self): #View Details of Employee
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(4)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)
        
        # My Info View
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() # menu my info
        time.sleep(4)        

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text

        self.assertIn('My Info', text_atas)
        self.assertEqual(text_bawah, 'Personal Details')

    def test_b_myinfo_add_nick(self): # Add Nickname for Employee
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(4)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)
        
        # My Info View
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() # menu my info
        time.sleep(4)

        # add nickname
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("PaulCol") # menu my info
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click() #button save
        time.sleep(3)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text

        self.assertIn('My Info', text_atas)
        self.assertEqual(text_bawah, 'Personal Details')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()