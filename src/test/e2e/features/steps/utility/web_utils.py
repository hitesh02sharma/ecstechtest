from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import  webdriver
myname ="Hitesh Sharma"

class WebUtils(object):


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def verify_logo(self, element_locator):

        try:
            element = self.wait.until(EC.presence_of_element_located(element_locator))
            if element is not None:
                print("ECS Logo visible on the home page")
        except:
                print("ECS Logo not visible on the home page")

    def click_button(self, button_locator):

        try:
            element = self.wait.until(EC.element_to_be_clickable(button_locator))
            element.click()
            print("Render the challenge button present and user is able to click on button successfully")
        except:
            print("Render the challenge button not present and user unable to on button")

    def get_elements(self, element_locator):

        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(element_locator))
            print("Button successfully clicked")
            return elements
        except:
            print("Unable to click the button")

    def sendkeys_for_submit_answer(self,element_locator,centerIndexValue):

        try:

            element = self.wait.until(EC.presence_of_element_located(element_locator))
            element.send_keys(centerIndexValue)
            print("")
        except:
            print("")

    def sendkeys_for_name(self,element_locator,name):

        try:

            element = self.wait.until(EC.presence_of_element_located(element_locator))
            element.send_keys(myname)
            print(f"Able to pass the candidate name {myname} successfully")
        except:
            print(f"Unable to pass the candidate name {myname}")
