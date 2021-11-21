from web_utils import WebUtils
from ecs_locators import *



class ECSPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.web_utils = WebUtils(driver)

    def verify_logo(self):
        self.web_utils.verify_logo(ECSPageLocators.ECS_LOGO)

    def render_challenge(self):
        self.web_utils.click_button(ECSPageLocators.RENDER_CHALLENGE_BUTTON)

    def name(self):
        self.web_utils.sendkeys_for_name(ECSPageLocators.SUBMIT_YOUR_NAME,None)

    def final_submit_answer(self):
        self.web_utils.click_button(ECSPageLocators.SUBMIT_ANSWERS_BUTTON)

    emptyList =[ECSPageLocators.SUBMIT_ANSWER_1_ENTER,ECSPageLocators.SUBMIT_ANSWER_2_ENTER, ECSPageLocators.SUBMIT_ANSWER_3_ENTER]
    def submit_answer(self,centerIndexValue, index):

        self.web_utils.sendkeys_for_submit_answer(self.emptyList[index],centerIndexValue)

    def get_challenge_data(self):
        data_array_list = []
        row_elements = self.web_utils.get_elements(ECSPageLocators.CHALLENGE_TABLE_ROW)
        for row in row_elements:
            data_array = row.text.split(" ")

            data_array_list.append([int(x) for x in data_array])

        return data_array_list

    def get_center_array(self, new_data_array):
        sum = 0

        sum_left = []
        for val in new_data_array:
            sum += val
            sum_left.append(sum)

        sum_right = []
        for val in new_data_array:
            sum_right.append(sum)
            sum -= val

        for i in range(len(sum_left)) :
            if sum_left[i] == sum_right[i]:
                print(f"Matching index is {i}.")
                break
        return i

    def list_of_Index(self,data_array_list):
        value_of_index=[]
        for l in data_array_list:
            value_of_index.append(self.get_center_array(l))
        return value_of_index





