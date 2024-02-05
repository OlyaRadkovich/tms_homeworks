import allure

from test_homework_24.src.bank_page import BankPage
from test_homework_24.src.constants import Host
from test_homework_24.src.main_page import MainPage


class TestGetCard:
    @allure.title("Оформление карты Альфа-банка через сайт Myfin.by")
    def test_get_card(self, driver):
        with allure.step("Проверка открытия главной страницы Myfin.by"):
            main_page = MainPage(driver)
        with allure.step("Навестись на раздел 'Карты' в хэдере"):
            main_page.header.hover()
            main_page.header.assert_element()
        with allure.step("Навестись на выпадающее меню"):
            main_page.drop_down_menu.hover()
        with allure.step("Наведение на меню удалось"):
            main_page.drop_down_menu.assert_element()
        with allure.step("Элемент в выпадающем меню найден"):
            main_page.red_card_button.assert_element()
        with allure.step("Кликнуть на элемент"):
            main_page.red_card_button.click()
        with allure.step("Переход на страницу Альфа-банка"):
            driver.switch_to.window(driver.window_handles[-1])
            assert driver.current_url == Host.RED_CARD_HOST
        bank_page = BankPage(driver)
        with allure.step("Найти строку ввода и ввести номер телефона"):
            bank_page.phone_input.assert_element()
            bank_page.phone_input.send_keys('291001010')
        with allure.step("Нажать кнопку подтверждения"):
            bank_page.confirm_button.click()
        with allure.step("Страница содержит кнопку регистрации"):
            bank_page.msi_button.assert_element()
        with allure.step("Страница содержит заголовок 'Оформление кредитной карты онлайн'"):
            bank_page.service_title.assert_element()
            assert bank_page.service_title.get_attribute() == "Оформление кредитной карты онлайн"
