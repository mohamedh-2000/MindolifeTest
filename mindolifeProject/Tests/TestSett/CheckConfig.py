from selenium.webdriver.support.wait import WebDriverWait
from mindolifeProject.Selenium.SeleniumBase import SeleniumBase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
def Chek_Config():
    class mind0lofe(SeleniumBase):
        selenium_base = SeleniumBase()
        driver = selenium_base.selenium_start('https://api.mindolife.com/')
        uname = driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
        uname.click()
        uname.clear()
        uname.send_keys("tsofen")
        uname.send_keys(Keys.ENTER)
        pw = driver.find_element(By.CSS_SELECTOR, 'input[type=password]')
        pw.click()
        uname.clear()
        pw.send_keys("tsofen@mindolife")
        pw.send_keys(Keys.ENTER)
        sleep(2)
        # page objct
        cog = driver.find_element(By.CLASS_NAME, 'js-right-sidebar')
        cog.click()
        sleep(2)
        wait = WebDriverWait(driver, 10)



