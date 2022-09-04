import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
       
    def test_a_leave_assign(self): # Assign Leave to an Employee
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() # klik menu Leave
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a").click() #klik tombol assign leave
        time.sleep(2)

        # Assign Leave
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("alice")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div/span").click() #alice duval
        time.sleep(2)       

        # Leave type
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[6]/span").click() #can-vacation
        time.sleep(2)  

        # Date
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[4]/div").click() #from date
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[10]/div").click() #to date
        time.sleep(2)

        # Partial Day
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[1]/div/div[2]/div/div[2]/div[2]/span").click() #allday
        time.sleep(2)
        
        # Duration
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/span").click() #halfday-morning
        time.sleep(2) 

        # Button Assign
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[6]/button").click()
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertTrue('Leave', text_atas)
        self.assertTrue(text_bawah, 'Leave List')

    def test_b_leave_approve(self): # Approve leave requests
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span").click() # klik menu Leave
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/button[1]").click()  # select request to approve
        time.sleep(2)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertIn('Leave', text_atas)
        self.assertEqual(text_bawah, 'Leave List')

    def test_c_leave_view(self): #  View List of Leave by Employee Name
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() # klik menu Leave
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("charlie")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span").click() # klik charlie carter
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]").click()
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text

        self.assertIn('Leave', text_atas)
        self.assertEqual(text_bawah, 'Leave List')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()