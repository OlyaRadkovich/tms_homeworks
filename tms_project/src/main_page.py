from tms_project.src.base_action import BaseElement
from tms_project.src.common_page import CommonPage


class MainPage(CommonPage):
    recommendations_xpath = '//*[@class="last-episodes-day__title"]'

    def __init__(self, driver):
        super().__init__(driver)

        # rand_index = random.randint(1, 80)
        # self.random_movie = BaseAction(driver, f'//*[@class="last-episodes-day"]/descendant:: a[{rand_index}]')
        self.xpath_for_random = BaseElement(driver,
                                           '//*[@class="last-episodes-day"]/descendant:: a')

        # мне пашанцуе
        self.lucky_me_button = BaseElement(driver, '//*[@id="random-filter"]')

        # ============================= Search parameters ===================================================

        self.submit_filter_button = BaseElement(driver,
                                               '//*[@id="submit-filter"]')

        # фильм или сериал
        self.search_by_type = BaseElement(driver,
                                         '//*[@class="custom-select select select-init"][1]')
        self.chosen_type_film = BaseElement(driver,
                                           '//*[@class="select-items"]/child::*[1]')
        self.chosen_type_serial = BaseElement(driver,
                                             '//*[@class="select-items"]/child::*[2]')

        # жанры
        self.search_by_genre = BaseElement(driver,
                                          '//*[@class="custom-select select select-init"][2]')
        self.genres = BaseElement(driver, '//*[@class="select-items"]')
        self.chosen_genre = BaseElement(driver,
                                       '//*[@class="select-items"]/child::*[contains(text(), "Спорт")]')

        # страны
        self.search_by_country = BaseElement(driver,
                                            '//*[@class="custom-select select select-init"][3]')
