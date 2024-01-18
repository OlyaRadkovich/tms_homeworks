from src.base_action import BaseAction
from src.base_page import BasePage


class CommonPage(BasePage, BaseAction):
    def __init__(self, driver):
        super().__init__(driver)

        # ======================= Elements of header ==================================

        self.header = BaseAction(driver, '//*[@id="header"]')
        self.logo = BaseAction(driver, '//*[@class="header-logo"]')
        self.header_menu = BaseAction(driver, '//*[@class="navigation-links"]')
        self.search_button = BaseAction(driver, '//*[@class="btn__search"]')
        self.search_field = BaseAction(driver, '//*[@id="search-top-field"]')
        self.search_submit = BaseAction(driver, '//*[@class="header-search__button-submit"]')
        self.movie_button = BaseAction(driver, '//*[@href="/Catalog?type=movie"]')
        self.serial_button = BaseAction(driver, '//*[@href="/Catalog?type=tv"]')
        self.anime_button = BaseAction(driver, '//*[contains (@href, "Анімэ")]')
        self.donation_button = BaseAction(driver, '//*[@class="navigation-links"]'
                                                  '/descendant::*[@href="https://www.patreon.com/kinakipa"]')
        self.sign_in_button = BaseAction(driver, '//*[contains (@href, "Account")]')

        # ======================= Elements of footer ==================================

        self.footer = BaseAction(driver, '//*[@class="footer"]')
        self.vk_link = BaseAction(driver, '//*[@href="https://vk.com/kinakipa"]')
        self.tg_link = BaseAction(driver, '//*[@href="https://t.me/kinakipaby"]')
        self.mail_link = BaseAction(driver, '//*[@href="mailto:kinakipasite@gmail.com"]')
        self.bot_link = BaseAction(driver, '//*[@href="https://t.me/kinakipa_site_bot"]')
        self.patreon_link = BaseAction(driver, '//*[@class="footer__contacts"]/'
                                               'descendant::*[@href="https://www.patreon.com/kinakipa"]')

        # ==============================================================================

        self.up_button = BaseAction(driver, '//*[@class="scroll-top-button visible"]')
        self.back_home_button = BaseAction(driver, '//*[@class="breadcrumbs"]/descendant::*[@href="/"]')
        self.searched_movie1 = BaseAction(driver, '//*[@class="catalog"]/descendant::a[1]')
