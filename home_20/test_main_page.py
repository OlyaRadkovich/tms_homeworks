# Написать параметризированный тест, который:
# 1 - открывает в любом браузере* сайты https://www.amazon.com/, https://www.apple.com/, https://www.google.com/
# 2 - Проверяет, что на сайте заголовке окна для сайта Амазона - Amazon, для Эпла - Apple, для Гугла - Google
# 3 - тест должен быть параметризированным. Т.е. должны быть две переменные url и page_title, которые меняются
# 4 - на каждый сайт запускается новый тест
# * Можете попробовать запускать разные браузеры на разные сайты, например: для Амазона и Эпла - Firefox,
# для Гугла - хром
# ** В конце теста можно делать скриншот страницы. Делается это через driver. save_screenshot()
# *** (для самых отчаянных!) Попробуйте написать фикстуру драйвера так, чтобы скриншот делался при падении.
# Падение можно организовать через raise Exception("Something is wrong") в теле теста


import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    with webdriver.Chrome(options) as driver:
        yield driver


class TestMainPage:
    @pytest.mark.parametrize("main_page, expected_title",
                             [("https://www.amazon.com/", "Amazon"),
                              ("https://www.apple.com/", "Apple"),
                              ("https://www.google.com/", "Google")])
    def test_main_page(self, main_page, expected_title, driver):
        driver.get(main_page)
        current_url = driver.current_url
        assert current_url in ["https://www.amazon.com/",
                               "https://www.apple.com/",
                               "https://www.google.com/"]
        assert expected_title in driver.title
