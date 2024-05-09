import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def selenium_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    search_ele = driver.find_element(By.NAME, "q")
    search_ele.send_keys("Amazon")
    search_ele.submit()
    time.sleep(5)
    driver.implicitly_wait(40)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, sel_driver):
    yield
    item = request.node
    driver = sel_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
