# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




#-----------------------------


# from mindolifeProject.Pages.LogInPages import LogInPages
# from time import sleep
# from mindolifeProject.Selenium.SeleniumBase import SeleniumBase
# from mindolifeProject.Pages.LogInPages import LogInPages





# class login_mindo(SeleniumBase):
#     driver = SeleniumBase()
#     mindo_life_website = driver.selenium_start('https://api.mindolife.com/')
#     user1 = LogInPages(driver)
#     user1.sent_user_name('iiii')
#     sleep(10)




#
# I apologize for any confusion. To clarify, in order to use the LogInPages class to send the username 'iiii' to the website, you need to do the following:
#
#     Create an instance of the Selenium webdriver, for example by using webdriver.Chrome(ChromeDriverManager().install())
#     Use the webdriver instance to open the website you want to log in to, by calling the get method on the webdriver instance and passing the URL of the website as an argument.
#     Create an instance of the LogInPages class and pass the webdriver instance to it as an argument.
#     Call the sent_user_name method on the LogInPages class instance, passing the desired username as an argument.
#     Close the browser after the test is done.
#
# Here is an example of how you could use the LogInPages class to send the username 'iiii' to the website:
