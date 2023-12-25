# Автоматизировать следующий кейс:
# 1. Открыть сайт https://myfin.by/
# 2. Навестись на раздел "Карты" в хедере
# 3. Нажать "Красная карта 2.0"
# 4. В поле "Номер мобильного телефона" ввести 299402265
# 5. Нажать кнопку "Подтвердить"
# Ожидаемый результат:
# - Появилась надпись "Пройдите идентификацию"
# - Появилась кнопка "Перейти в МСИ"
# --- со звездочкой ---
# - Проверить, что кнопка "Перейти в МСИ" цвета #ef3124

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webcolors


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    with webdriver.Chrome(options) as driver:
        yield driver


def assert_element(driver, xpath, clickable=False):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    if clickable:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    result = driver.find_element(By.XPATH, xpath)
    return result


def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)

    element.click()


class TestMyfin:

    def test_choose_red_card(self, driver):
        driver.get("https://myfin.by")
        header_xpath = '//*[contains(@class,"--straight") and contains(@href, "cards")]'
        drop_down_menu_xpath = '//*[text()="Онлайн оформление карты"]'
        red_card_xpath = '//*[contains(@data-link, "creditcard.alfa-bank.by")][1]'
        phone_input_xpath = '//*[@type="tel"]'
        confirm_button_xpath = '//*[@type="submit"]'
        suggestion_xpath = '//*[@class="title"]'
        msi_button_xpath = '//*[@type="button"]'

        header = assert_element(driver, header_xpath)
        drop_down_menu = assert_element(driver, drop_down_menu_xpath)
        red_card = assert_element(driver, red_card_xpath)
        action = ActionChains(driver)
        action.move_to_element(header).perform()
        action.move_to_element(drop_down_menu).perform()
        red_card.click()
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == "https://creditcard.alfa-bank.by/RKK?channel=0006"

        phone_input = assert_element(driver, phone_input_xpath)
        phone_input.send_keys('291001010')
        confirm_button = assert_element(driver, confirm_button_xpath)
        confirm_button.click()

        for _ in range(10):
            suggestion = assert_element(driver, suggestion_xpath)
            suggestion_text = suggestion.get_attribute("textContent")
            if suggestion_text == "Пройдите идентификацию":
                break
            sleep(1)
        else:
            raise Exception("Предложение пройти идентификацию не появилось")

        msi_button = assert_element(driver, msi_button_xpath)
        color = msi_button.value_of_css_property('background-color')
        color = color[5:-4].split(",")
        rgb_colors = list(map(int, color))
        hex_color = webcolors.rgb_to_hex(rgb_colors)
        assert hex_color == '#ef3124'

