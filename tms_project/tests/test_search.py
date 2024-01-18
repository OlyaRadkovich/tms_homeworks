from selenium.common import NoSuchElementException

from tms_project.src.common_page import CommonPage
from tms_project.src.main_page import MainPage
from tms_project.src.movie_page import MoviePage


def search_and_check(driver, word, element):
    """" Данная функция передаёт в строку поиска слово, переходит
    на страницу с результатами, далее переходит на страницу одного
    из фильмов и проверяет, содержится ли данное слово в соответствующем
    разделе информации о фильме.
    Если вводится беспорядочное сочетание букв, функция вызывает исключение,
    т.к. сайт открывает страницу без контента"""

    cp = CommonPage(driver)
    mvp = MoviePage(driver)
    try:
        cp.search_button.click()
        cp.search_field.send_keys(word)
        cp.search_submit.click()
        driver.switch_to.window(driver.window_handles[-1])
        mvp.searched_movie1.click()
        driver.switch_to.window(driver.window_handles[-1])
        text_content = element.get_attribute().lower()
        assert word in text_content
    except NoSuchElementException:
        print(f'Search for the "{word}" did not return any results')
        pass


class TestSearch:
    # Проверяем поиск по названию/части названия
    def test_input_word(self, driver):
        mvp = MoviePage(driver)
        for word in ['black', 'potter', 'king', 'пірат', 'клуб', 'fashooshoo', 'прыгоды']:
            search_and_check(driver, word, mvp.movie_title)

    # Проверяем поиск по имени режиссёра или актёра (в данном случае поиск возможен только на кириллице)
    def test_input_name(self, driver):
        mvp = MoviePage(driver)
        for word in ['джармуш', 'андэрсан', 'джэф брыджэс', 'olli', 'суінтан']:
            search_and_check(driver, word, mvp.about_movie)

    # Кликаем 5 раз на кнопку "Мне пашанцуе!" и проверяем, что каждый раз открывается новая страница
    def test_random_search(self, driver):
        mp = MainPage(driver)
        url_list = []
        for _ in range(5):
            mp.lucky_me_button.click()
            driver.switch_to.window(driver.window_handles[-1])
            url = driver.current_url
            url_list.append(url)
            driver.back()
        url_set = set(url_list)
        assert len(url_list) == len(url_set)

    def test_search_with_filters(self, driver):
        mp = MainPage(driver)
        mp.search_by_type.click()
        mp.chosen_type_film.click()
        mp.search_by_genre.click()
        mp.genres.hover()
        mp.chosen_genre.click()
        mp.submit_filter_button.click()
        driver.switch_to.window(driver.window_handles[-1])
