import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def assert_element(self, clickable=False):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath)))

        if clickable:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath)))

    def click(self):
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.click()

    def cool_click(self):
        element = self.driver.find_element(By.XPATH, self.xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", element)

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.xpath)
        actions.move_to_element(element).perform()

    def send_keys(self, keys):
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.send_keys(keys)

    def get_attribute(self):
        element = self.driver.find_element(By.XPATH, self.xpath)
        return element.get_attribute("textContent")

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def get_random_element_by_xpath(self):
        elements = self.driver.find_elements(By.XPATH, self.xpath)
        number_of_elements = len(elements)
        random_index = random.randint(0, number_of_elements)
        # random_xpath = f"[{xpath}][{random_index}]"
        return f"{self.xpath}[{random_index}]"
