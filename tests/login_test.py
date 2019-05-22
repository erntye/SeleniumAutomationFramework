import time
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
from datetime import datetime


#python -m pytest --html=reports/report1.html --self-contained-html

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()


    def test_logout(self):
        try:
            driver= self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            time.sleep(5)
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as e:
            print("there was an assertion error")
            print(e)
            testName = utils.whoami() + str(datetime.now())
            allure.attach(self.driver.get_screenshot_as_png(), name=testName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Ernest/PycharmProjects/AutomationFramework/screenshots/" + testName +'.png')
            raise
        except:
            print("there was an exception")
            raise
        else:
            print("no exception")
        finally:
            print("I am inside finally")
