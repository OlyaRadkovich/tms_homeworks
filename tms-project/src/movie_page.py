from src.base_action import BaseAction
from src.common_page import CommonPage


class MoviePage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.movie_title = BaseAction(driver, '//*[@class="about-serial-header__subtitle"]')
        self.about_movie = BaseAction(driver, '//*[@class ="about-serial-right"]')
