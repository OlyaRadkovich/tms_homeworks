import pytest
from selenium import webdriver

from src.constants import Host
from src.main_page import MainPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    with webdriver.Chrome() as driver:
        yield driver


# @pytest.fixture
# def driver(browser_name):
#     if browser_name == 'chrome':
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#         with webdriver.Chrome() as driver:
#             yield driver
#     elif browser_name == 'edge':
#         options = webdriver.EdgeOptions()
#         options.add_argument("--window-size=1920,1080")
#         with webdriver.Edge() as driver:
#             yield driver
#     else:
#         raise ValueError(f'Unsupported browser: {browser_name}')
#
#
# def pytest_addoption(parser):
#     parser.addoption('--browser', action='store',
#                      default='chrome', help='Browser name')
#
#
# def pytest_generate_tests(metafunc):
#     if "browser_name" in metafunc.fixturenames:
#         metafunc.parametrize("browser_name", [metafunc.config.getoption("browser")])


@pytest.fixture(autouse=True)
def open_main_page(driver, request):
    if request.node.get_closest_marker("skip_main_page"):
        pytest.skip("Skipping main page for this test")
    else:
        main_page = MainPage(driver)
        main_page.driver.get(Host.KIPA_MAIN)
