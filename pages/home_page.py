from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Locators:
    FREE_VPN_XPATH = (By.XPATH, "//div[@class='home-hero__content']/h1")


class HomePage(BasePage):
    def find_text_element(self):
        return self.find_element(Locators.FREE_VPN_XPATH).text
