import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
class SeleniumBase():
    def __init__(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    def selenium_start(self, url):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        return driver

    def selenium_end(self):
        self.driver.quit()
class LogInPages:
    def __init__(self, driver):
        self.driver = driver
    def sent_user_name(self, username):
        uname = self.driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
        uname.click()
        uname.clear()
        uname.send_keys(username)
        uname.send_keys(Keys.ENTER)




    def sent_password(self, password):
        passwd = self.driver.find_element(By.CSS_SELECTOR, 'input[type=password]')
        passwd.click()
        passwd.clear()
        passwd.send_keys(password)
        passwd.send_keys(Keys.ENTER)

class Login(SeleniumBase):
    def __init__(self):
        super().__init__()

    def login(self, url, username, password):
        self.selenium_start(url)
        user = LogInPages(self.driver)
        user.sent_user_name(username)
        user.sent_password(password)

    def end(self):
        self.selenium_end()


@pytest.fixture
def login():
    login_test = Login()
    yield login_test


