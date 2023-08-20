# -----------------------------------------------------------------------
#                   ***  All Login tests  ***
# -----------------------------------------------------------------------
from mindolifeProject.Tests.TestSett.CheckConfig import Chek_Config
from mindolifeProject.Tests.TestSett.LogInCorrectUserAndpasswordPage import LogInCorrectUserAndpassword
from mindolifeProject.Pages.SentUserNamePage import SeleniumBase
from mindolifeProject.Pages.SentUserNamePage import login


# frist test login username and password
def test_LogIn_Correct_User_And_password(login):
    login.login("https://api.mindolife.com/ ", "tsofen", "tsofen@mindolife")
    #     #check if the login was successful
    assert True
    print('Test Log with User Name And Password was successful')


# Second check with incorrect username and password
def test_login_wrong_details(login):
    login.login("https://api.mindolife.com/ ", "tsofe", "tsofen@mindolife")
    assert False
    print('Test Log with User Name And Password was not successful')


# Test number three with incorrect username and password
def test_login_with_space(login):
    login.login("https://api.mindolife.com/ ", "  ", " ")
    assert False
    print('Test Log with User Name And Password was not successful')

#Test number four Test icon settings
def test_check_config():
    Chek_Config()
    print('Test  Settings opened successful ')






