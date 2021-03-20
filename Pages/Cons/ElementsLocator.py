from selenium.webdriver.common.by import By


class MainPageLocators:
    search_icon = (By.ID, 'io.plaidapp:id/menu_search')
    more_options = (By.XPATH, '//android.widget.ImageView[@content-desc="More options"]')
    login_designer = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout')
    about = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout')