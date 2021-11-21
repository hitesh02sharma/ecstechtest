from selenium.webdriver.common.by import By


class ECSPageLocators:
    RENDER_CHALLENGE_BUTTON = (By.XPATH, "//button[.='Render the Challenge']")
    CHALLENGE_TABLE_ROW = (By.XPATH, "//table/tbody/tr")
    SUBMIT_ANSWER_1_ENTER = (By.XPATH, "//input[@data-test-id='submit-1']")
    SUBMIT_ANSWER_2_ENTER = (By.XPATH, "//input[@data-test-id='submit-2']")
    SUBMIT_ANSWER_3_ENTER = (By.XPATH, "//input[@data-test-id='submit-3']")
    SUBMIT_YOUR_NAME = (By.XPATH, "//input[@data-test-id='submit-4']")
    SUBMIT_ANSWERS_BUTTON = (By.XPATH, "//*[@id='challenge']/div/div/div[2]/div/div[2]/button/div/div")
    ECS_LOGO =(By.XPATH,"//img[contains(@src,'/static/media/logo.2c7b0c96.png')]")
