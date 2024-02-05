from test_homework_24.src.base_element import BaseElement
from test_homework_24.src.base_page import BasePage


class BankPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.phone_input = BaseElement(driver, '//*[@type="tel"]')
        self.confirm_button = BaseElement(driver, '//*[@type="submit"]')
        self.msi_button = BaseElement(driver, '//*[@type="button"]')
        self.service_title = BaseElement(driver,
                                         '//*[@class = "alfaPageFrame redirectPage"]/descendant::*[@class="pageTitle"]')
