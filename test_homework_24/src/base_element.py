import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
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
