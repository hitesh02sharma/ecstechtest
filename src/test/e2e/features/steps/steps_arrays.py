from behave import *
from ecs_page_object import *

use_step_matcher("re")


@given("User is able to access ECS application")
def step_verify_access_to_ecs(context):
    # verify if the page is loaded with the ECS logo
    ecs_page = ECSPage(context.driver)
    ecs_page.verify_logo()


@when("User should able to click on Render the challenge button")
def render_challenge(context):
    # verify the button presence and user should able to click on render the challenge button
    ecs_page = ECSPage(context.driver)
    ecs_page.render_challenge()
    context.data_array_list = ecs_page.get_challenge_data()


@step("User should able to find correct index value and able to enter the index value for challenge 1 and challenge 2 "
      "and challenge 3 and name")
def step_impl(context):
    # Logic to find the correct index value & submission of input values
    ecs_page = ECSPage(context.driver)
    context.indexValue = ecs_page.list_of_Index(context.data_array_list)
    for i, j in enumerate(context.indexValue):
        ecs_page.submit_answer(j, i)
    ecs_page.name()


@then("User should able to submit the answers successfully")
def step_impl(context):
    # verify that user should able to submit the answers
    ecs_page = ECSPage(context.driver)
    ecs_page.final_submit_answer()
