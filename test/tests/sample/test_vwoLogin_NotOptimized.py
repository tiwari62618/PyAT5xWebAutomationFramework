from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os
from test.utils import Utils
from test.utils.Utils import take_screen_shot


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1-Negative TC- VWO Login with invalid creds.")
@allure.feature("VWO Login with invalid creds")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():

    # if os.getenv("BROWSER")=="chrome":
    #     chrome_options=Options()
    #     chrome_options.add_argument("--incognito")
    #     driver=webdriver.Chrome(chrome_options)
    #     driver.get(os.getenv("URL"))
    # elif os.getenv("BROWSER")=="edge":
    #     chrome_options=Options()
    #     chrome_options.add_argument("--incognito")
    #     driver=webdriver.Edge(chrome_options)
    #     driver.get(os.getenv("URL"))
    # elif os.getenv("BROWSER")=="firefox":
    #     chrome_options=Options()
    #     chrome_options.add_argument("--incognito")
    #     driver=webdriver.Firefox(chrome_options)
    #     driver.get(os.getenv("URL"))
    # else:
    #     print("Browser not found!")
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options=Options()
            chrome_options.add_argument("--incognito")
            driver=webdriver.Chrome(options=chrome_options)

        case "edge":
            edge_options=Options()
            edge_options.add_argument("--inprivate")
            driver=webdriver.Edge(options=edge_options)

        case "firefox":
            firefox_options=Options()
            firefox_options.add_argument("-private")
            driver=webdriver.Firefox(options=firefox_options)

        case _:
            print("Browser not found!")
            exit(1)

    driver.get(os.getenv("URL"))

    email_web_element=driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element=driver.find_element(By.NAME,"password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_element=driver.find_element(By.ID,"js-login-btn")
    submit_btn_element.click()

    time.sleep(3)

    error_message_web_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)

    take_screen_shot(driver=driver,name="vwoLoginFailed")


    assert error_message_web_element.text==os.getenv("error_message_expected")
    time.sleep(5)

    driver.quit()


