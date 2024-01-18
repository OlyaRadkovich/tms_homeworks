from tms_project.src.base_action import BaseElement
from tms_project.src.base_page import BasePage


class CommonPage(BasePage, BaseElement):
    def __init__(self, driver):
        super().__init__(driver)

        # ======================= Elements of header ==================================

        self.header = BaseElement(driver, '//*[@id="header"]')
        self.logo = BaseElement(driver, '//*[@class="header-logo"]')
        self.header_menu = BaseElement(driver, '//*[@class="navigation-links"]')
        self.search_button = BaseElement(driver, '//*[@class="btn__search"]')
        self.search_field = BaseElement(driver, '//*[@id="search-top-field"]')
        self.search_submit = BaseElement(
            driver, '//*[@class="header-search__button-submit"]'
        )
        self.movie_button = BaseElement(
            driver, '//*[@href="/Catalog?type=movie"]'
        )
        self.serial_button = BaseElement(driver, '//*[@href="/Catalog?type=tv"]')
        self.anime_button = BaseElement(driver, '//*[contains (@href, "Анімэ")]')
        self.donation_button = BaseElement(
            driver,
            (
                '//*[@class="navigation-links"]'
                '/descendant::*[@href="https://www.patreon.com/kinakipa"]'
            ),
        )
        self.sign_in_button = BaseElement(
            driver, '//*[contains (@href, "Account")]'
        )

        # ======================= Elements of footer ==================================

        self.footer = BaseElement(driver, '//*[@class="footer"]')
        self.vk_link = BaseElement(
            driver, '//*[@href="https://vk.com/kinakipa"]'
        )
        self.tg_link = BaseElement(
            driver, '//*[@href="https://t.me/kinakipaby"]'
        )
        self.mail_link = BaseElement(
            driver, '//*[@href="mailto:kinakipasite@gmail.com"]'
        )
        self.bot_link = BaseElement(
            driver, '//*[@href="https://t.me/kinakipa_site_bot"]'
        )
        self.patreon_link = BaseElement(
            driver,
            (
                '//*[@class="footer__contacts"]/'
                'descendant::*[@href="https://www.patreon.com/kinakipa"]'
            ),
        )

        # ==============================================================================

        self.up_button = BaseElement(
            driver, '//*[@class="scroll-top-button visible"]'
        )
        self.back_home_button = BaseElement(
            driver, '//*[@class="breadcrumbs"]/descendant::*[@href="/"]'
        )
        self.searched_movie1 = BaseElement(
            driver, '//*[@class="catalog"]/descendant::a[1]'
        )
