import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

# POSITIVE CASE        
    def test_a_admin_search_user(self): # search with username
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # klik menu Admin
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Joe.Root") # isi username
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def test_b_admin_search_user_role(self): # search with user role admin
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(4)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() # select user role
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span").click() # Select Admin
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def test_c_admin_search_user_role(self): # search with user role ess
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(4)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() # select user role
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/span").click() # select ESS
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def test_d_admin_search_valid_employee(self): # search user by valid employee name
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(4)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys("Joe") # employee name
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div/span").click() # select Joe Root
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def test_e_admin_add_user(self): # add an user
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(4)

        # Add User
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("lisa")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span").click() # employee name
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("lisaandrews1") # employee username
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("LisAN1234_") # employee password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("LisAN1234_") # employee comfirm password
        time.sleep(2)

        # User Role & Status          
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click() # select role
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span").click() # select admin
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/i").click() # select status
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span").click() # select enabled
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # klik tombol save
        time.sleep(2)

# NEGATIVE CASE
    def test_f_admin_search_invalid_employee(self): # search user by invalid employee name
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys("lalala") # invalid employee name
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def test_g_admin_search_no_data(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(5)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik menu Admin
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").click # username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").click # employee name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(2)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('System Users', text_atas)
        self.assertTrue(text_bawah, 'Record Found')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()