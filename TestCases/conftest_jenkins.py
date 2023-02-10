import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = dict(
        platformName="iOS",
        deviceName="iPhone 14",
        platformVersion="16.2",
        bundleId="com.example.apple-samplecode.UICatalog",
        isHeadless=True
    )
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
