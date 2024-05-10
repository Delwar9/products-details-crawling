from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class Utils:

    def find_element_or_none(self, driver, locator: tuple[str, str], wait_in_seconds: float = 1):
        try:
            element = WebDriverWait(driver, wait_in_seconds).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            return None

    def find_elements_or_none(self, driver, locator: tuple[str, str], wait_in_seconds: float = 1):
        try:
            elements = WebDriverWait(driver, wait_in_seconds).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            return None

    def scroll_to_element(self, driver, web_element=None):
        try:
            actions = ActionChains(driver)
            actions.scroll_to_element(web_element)
            actions.perform()
            return True
        except:
            return False

    def scroll_to_percentage(self, driver, percentage):
        try:
            total_height = driver.execute_script("return document.body.scrollHeight")
            scroll_to_position = total_height * percentage / 100
            driver.execute_script(f"window.scrollTo(0, {scroll_to_position});")
            return True
        except:
            return False

    def write_dict_to_csv(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
