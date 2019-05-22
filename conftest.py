import pytest


# automatically adds CLI arguments
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="type in browser name")


# usefixtures automatically checks conftest
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser =="chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            executable_path="C:/Users/Ernest/PycharmProjects/AutomationFramework/drivers/chromedriver.exe")
    elif browser == "firefox":
        print("too bad")
    driver.implicitly_wait(5)
    driver.maximize_window()
    #sending driver to class driver
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")