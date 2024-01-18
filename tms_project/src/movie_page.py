from tms_project.src.base_action import BaseElement
from tms_project.src.common_page import CommonPage


class MoviePage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.movie_title = BaseElement(driver, '//*[@class="about-serial-header__subtitle"]')
        self.about_movie = BaseElement(driver, '//*[@class ="about-serial-right"]')
