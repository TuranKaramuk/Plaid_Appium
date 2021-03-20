from appium import webdriver
import os
from pathlib import Path

main_dir = Path(__file__).parents[1]
app_dir = os.path.join(main_dir, "app_binaries")
app_name = "plaid-debug.apk"

"""
Desired Capabilities
"""

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": os.path.join(app_dir, app_name),
  "appPackage": "io.plaidapp",
  "appWaitActivity": "io.plaidapp.Launcher"
}


# Create Driver
class Session:

    @staticmethod
    def start_web_driver_session():
        driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=desired_cap)
        driver.implicitly_wait(30)
        return driver
