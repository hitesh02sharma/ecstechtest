from selenium import webdriver
from behave import fixture
import os
import sys

sys.path.append(os.path.abspath(__file__ + "/../steps/PageObjects"))
sys.path.append(os.path.abspath(__file__ + "/../steps/utility"))


def before_all(context):
    chromedriver_path = os.path.abspath(__file__ + "/../../config/chromedriver.exe")
    context.driver = webdriver.Chrome(chromedriver_path)
    print()
    # Launch browser and load the URL
    pass


def before_scenario(context, scenario):
    # Load the URL
    context.driver.get("http://localhost:3000")
    print()
    pass


def after_scenario(context, scenario):
    pass


def after_all(context):
    pass

@fixture
def driver(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    chromedriver_path = os.path.abspath(__file__ + "/../config/chromedriver.exe")
    context.driver = webdriver.Chrome(chromedriver_path)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()