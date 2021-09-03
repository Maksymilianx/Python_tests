import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
