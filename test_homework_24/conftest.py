import allure
import pytest
from selenium import webdriver
from test_homework_24.src.main_page import MainPage
from test_homework_24.src.constants import Host


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    with webdriver.Chrome() as driver:
        yield driver


@pytest.fixture(autouse=True)
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.driver.get(Host.MY_FIN)
