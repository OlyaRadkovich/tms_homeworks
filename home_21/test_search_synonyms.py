# - Зайти на сайт https://www.thesaurus.com/
# - В поле поиска ввести love
# - Нажать иконку поиска
# - Найти 6 синоним слова love
# - вывести его в консоль
# * Для любителей полазить по верстке: вывести на экран все синонимы слова love


from selenium.webdriver.common.by import By


class TestClass:
    def test_search_synonyms(self, driver):
        driver.get('https://www.thesaurus.com')
        search_line = driver.find_element(By.XPATH, "//*[@id='global-search']")
        search_line.send_keys("love")
        search_button = driver.find_element(By.XPATH, "//*[@type='submit' and @data-type='button']")
        search_button.click()
        synonyms_6 = driver.find_element(By.XPATH, "//*[contains(@href, 'www.thesaurus.com/browse/friendship')]")
        print(synonyms_6.text)
        print('')  # для красоты
        relevant_synonyms = driver.find_elements(By.XPATH, "//*[contains(@class, 'ESLI_')]")
        for synonyms in relevant_synonyms:
            print(synonyms.text)
