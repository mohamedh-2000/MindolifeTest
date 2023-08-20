from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mindolifeProject.Selenium.SeleniumBase import SeleniumBase


# func LogInCorrectUserAndpassword open mindolife page
def LogInCorrectUserAndpassword():
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



