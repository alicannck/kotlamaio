from selenium import webdriver    
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from time import sleep  
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


class kotlamaio:
    
    def girdi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("1")
        
        soyisim = driver.find_element(By.ID,"password")
        soyisim.send_keys("1")
        sleep(2)
        button = driver.find_element(By.ID,"login-button")
        button.click()
        ErrorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testsonucu = ErrorMessage.text == "Hatalı Giriş"
        print(f"1. TEST SONUCU: {testsonucu}") # burada yaptığımız yukarıda alınan error mesajı (hatalı giriş) se |test sonucuc : true| olur
        

    print("**********************************************")
                    # ÖDEV

    def hepsibos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        isim = driver.find_element(By.NAME,"user-name")
        isim.send_keys("")

        soyisim = driver.find_element(By.ID,"password")
        soyisim.send_keys("")

        button = driver.find_element(By.ID,"login-button")
        button.click()

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test2 = errorMessage.text == "Epic sadface: Username is required"
        print(f"2. TEST SONUCU {test2}")

    
    print("*****************************************")


    def sifrebos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")

        soyisim = driver.find_element(By.ID,"password")
        soyisim.send_keys("")

        button = driver.find_element(By.ID,"login-button")
        button.click()

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test3 = errorMessage.text == "Epic sadface: Password is required"
        print(f"3. TEST SONUCU: {test3}")


    print("*************************************************")

    def hepsigirili(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("locked_out_user")

        soyisim = driver.find_element(By.ID,"password")
        soyisim.send_keys("secret_sauce")

        button = driver.find_element(By.ID,"login-button")
        button.click()

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test4 = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"4. TEST SONUCU: {test4}")
    
    print("********************************************************")


    def girisistiyor(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)

        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")

        soyisim = driver.find_element(By.ID,"password")
        soyisim.send_keys("secret_sauce")

        button = driver.find_element(By.ID,"login-button")
        button.click()
        sleep(2)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)
        print("5. TEST SONUCU ")
 









cikti = kotlamaio()
cikti.girdi()
cikti.hepsibos()
cikti.sifrebos()
cikti.hepsigirili()
cikti.girisistiyor()

