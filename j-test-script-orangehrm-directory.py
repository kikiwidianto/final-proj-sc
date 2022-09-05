import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # def test_a_directory_view(self): #View Directory Pages
    #     # steps
    #     browser = self.browser #buka web browser
    #     browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
    #     time.sleep(2)
    #     browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
    #     time.sleep(2)
    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
    #     time.sleep(3)

    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a").click() # klik menu Directory
    #     time.sleep(5)
        
    #     # validasi
    #     text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    #     text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

    #     self.assertIn('Directory', text_atas)
    #     self.assertEqual(text_bawah, 'Directory')

    # def test_b_directory_search_valid(self): # Search Directory by 'Employee Name'
    #     # steps
    #     browser = self.browser #buka web browser
    #     browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
    #     time.sleep(6)
    #     browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
    #     time.sleep(2)
    #     browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
    #     time.sleep(2)
    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
    #     time.sleep(3)

    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a").click() # klik menu Directory
    #     time.sleep(5)

    #     # Directory - Employee Name
    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("joe")
    #     time.sleep(3)
    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span").click()
    #     time.sleep(3)
    #     browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
    #     time.sleep(3)
        
    #     # validasi
    #     text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    #     text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/p[1]").text

    #     self.assertIn('Directory', text_atas)
    #     self.assertEqual(text_bawah, 'Joe Root')

    def test_c_directory_search_invalid(self): # Search employee by invalid 'Employee Name'
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(6)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a").click() # klik menu Directory
        time.sleep(5)

        # Directory - Employee Name
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("lalala")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
        time.sleep(3)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertIn('Directory', text_atas)
        self.assertTrue(text_bawah, 'No Records Found')

    def test_d_directory_search_nodata(self): # Search employee no data
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a").click() # klik menu Directory
        time.sleep(5)

        # Directory - Employee Name
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
        time.sleep(3)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertIn('Directory', text_atas)
        self.assertTrue(text_bawah, 'No Records Found')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()