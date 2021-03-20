from Base.session import Session
from app.Application import Application


def before_scenario(context, scenario):

    context.driver = Session.start_web_driver_session()
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
