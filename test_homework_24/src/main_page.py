from test_homework_24.src.base_element import BaseElement
from test_homework_24.src.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.header = BaseElement(driver, '//*[contains(@class,"--straight") and contains(@href, "cards")]')
        self.drop_down_menu = BaseElement(driver, '//*[text()="Онлайн оформление карты"]')
        self.red_card_button = BaseElement(driver, '//*[contains(@data-link, "creditcard.alfa-bank.by")][1]')
