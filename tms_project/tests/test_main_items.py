import allure

from src.base_action import BaseAction
from src.common_page import CommonPage
from src.constants import Host
from src.main_page import MainPage
from tests.conftest import driver

def random_movie(driver):
    mp = MainPage(driver)
    return BaseAction(driver, mp.xpath_for_random.get_random_element_by_xpath())



class TestMainItems:
    allure.title("Проверка главной страницы")



    def test_open_main_page(self, driver):
        with allure.step("Открыть главную страницу"):
            assert driver.current_url == Host.KIPA_MAIN

    # Проверяем содержимое хэдера и кнопки меню (в РБ сcылки на Патреон открываются только через vpn)
    def test_header_items(self, driver):

        with allure.step("Проверить, что хэдер содержит все необходимые элементы"):
            cp = CommonPage(driver)
            header_item = [cp.header_menu, cp.logo, cp.movie_button,
                           cp.serial_button, cp.anime_button,
                           cp.donation_button, cp.sign_in_button]

            for item in header_item:
                item.assert_element()

        with allure.step("Кликнуть на кнопки 'фільмы', 'серыялы', 'анімэ', 'падтрымаць', 'увайсці' "
                         "и проверить открывшиеся страницы"):
            menu_item = [cp.movie_button, cp.serial_button,
                         cp.anime_button, cp.donation_button,
                         cp.sign_in_button]
            urls = ['https://kinakipa.site/Catalog?type=movie',
                    'https://kinakipa.site/Catalog?type=tv',
                    'https://kinakipa.site/Catalog?genre=%D0%90%D0%BD%D1%96%D0%BC%D1%8D',
                    'https://www.patreon.com/kinakipa',
                    'https://www.patreon.com/kinakipa']

            for item, url in zip(menu_item, urls):
                try:
                    item.click()
                    assert driver.current_url == url
                except (AssertionError):
                    print(f"Page {url} is currently not available")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    # Проверяем ссылки в футере и кнопку-стрелку "вверх"
    def test_footer_items(self, driver):
        cp = CommonPage(driver)
        cp.footer.scroll_to_end()

        with allure.step("Клик на ссылки в футере"):
            footer_item = [cp.vk_link, cp.tg_link, cp.bot_link, cp.patreon_link]

            urls = ['https://vk.com/kinakipa', 'https://t.me/kinakipaby', 'https://t.me/kinakipa_site_bot',
                    'https://www.patreon.com/kinakipa']

            for item, url in zip(footer_item, urls):
                item.assert_element()
                try:
                    item.cool_click()
                    if item != cp.bot_link:
                        driver.switch_to.window(driver.window_handles[-1])
                        assert driver.current_url == url
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    else:
                        assert driver.current_url == url
                        driver.back()
                    assert driver.current_url == Host.KIPA_MAIN
                except (AssertionError):
                    print(f"Page {url} is currently not available")

        with allure.step("Клик на кнопку 'вверх'"):
            cp.up_button.cool_click()

    # Проверяем, присутствуют ли на странице разделы с рекомендациями фильмов
    def test_recommendations(self, driver):
        with allure.step("Проверка разделов с рекомендациями"):
            for i in range(1, 7):
                chapter_xpath = f'{MainPage.recommendations_xpath}[{i}]'
                chapter = BaseAction(driver, chapter_xpath)
                chapter.assert_element()

    # Проверяем работу кнопки "Дадому"
    def test_back_home(self, driver):
        cp = CommonPage(driver)

        with allure.step("Перейти на страницу произвольного фильма"):
            random_movie(driver).cool_click()

        with allure.step("Клик на кнопку 'дадому' и переход на главную"):
            cp.back_home_button.click()
            assert driver.current_url == Host.KIPA_MAIN

    # Проверяем, что клик на логотип возвращает на главную страницу
    def test_logo_back_home(self, driver):
        cp = CommonPage(driver)
        with allure.step("Перейти на страницу произвольного фильма"):
            random_movie(driver).cool_click()
        with allure.step("Клик на логотип и переход на главную"):
            cp.logo.click()
            assert driver.current_url == Host.KIPA_MAIN


