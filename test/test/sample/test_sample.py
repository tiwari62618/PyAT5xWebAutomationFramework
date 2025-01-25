import pytest
import allure
import time

from selenium import webdriver

@allure.title("Dry run of the framework 1")
@allure.description("Verify that Dry run is working 1")
@allure.feature("TC#0 - Sample Test Run.")
def test_sample_pass():
    print("Hello Sample")
    assert True == True

@allure.title("Dry run of the framework 2")
@allure.description("Verify that Dry run is working 2")
@allure.feature("TC#1 - Sample Failed Run.")
def test_sample_fail():
    print("Hello Sample")
    assert True == False


