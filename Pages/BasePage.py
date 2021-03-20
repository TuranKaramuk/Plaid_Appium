class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def input(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
