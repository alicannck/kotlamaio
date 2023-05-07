from selenium import webdriver    
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from time import sleep  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date



class Test_deneme:
    

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)


    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locator))



    def test_deneme1(self): # bu 1. madde (isim ve şifre boş)

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_deneme_1.png")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Username is required"
    


    def test_deneme2(self):

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("standard_user")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_deneme_2.png")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Password is required"
    


    def test_deneme3(self):

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("locked_out_user")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_deneme_3.png")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    


    def test_deneme4(self):

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("standard_user")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
    
        self.driver.save_screenshot(f"{self.folderPath}/test_deneme_4.png")



    def test_Yenideneme1(self):

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_Yenideneme_1.png")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Username is required"
    


    def test_Yenideneme2(self): 
        
        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys("standard_user")

        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("")

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")

        self.driver.save_screenshot(f"{self.folderPath}/test_Yenideneme_2.png")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    


    @pytest.mark.parametrize("username,password",[("1","1"),("2","2"),("ad-deneme","soyad-deneme")])
    def test_Multideneme(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        name = self.driver.find_element(By.ID,"user-name")
        name.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passw = self.driver.find_element(By.ID,"password")
        passw.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        button = self.driver.find_element(By.ID,"login-button")
        button.click()
    
        self.driver.save_screenshot(f"{self.folderPath}/test_Multideneme_1_{username}-{password}.png")
    