from Pages.MainPage import MainPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
