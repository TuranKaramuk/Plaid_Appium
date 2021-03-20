from Pages.BasePage import BasePage
from Pages.Cons.ElementsLocator import MainPageLocators
import time


class MainPage(BasePage):
    def tap_search(self):
        self.click(*MainPageLocators.search_icon)

    def verify_search_icon(self):
        search_icon = self.find_element(*MainPageLocators.search_icon)
        assert search_icon.is_displayed()

    def tap_more_options(self):
        self.click(*MainPageLocators.more_options)

    def verify_log_in_to_designer_news_displayed(self):
        element = self.find_element(*MainPageLocators.login_designer)
        assert element.is_displayed()

    def verify_about_displayed(self):
        element = self.find_element(*MainPageLocators.about)
        assert element.is_displayed()

