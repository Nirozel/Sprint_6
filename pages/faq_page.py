from selenium.webdriver.common.by import By


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class FaqPage:
    def __init__(self, driver):
        self.driver = driver

    def get_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    def get_open_question_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    def click_question(self, index):
        self.driver.find_element(*self.get_question_locator(index)).click()

    def is_open_question(self, index):
        self.driver.find_element(*self.get_question_locator(index)).click()

    def is_answer_displayed(self, index):
        return self.driver.find_element(*self.get_answer_locator(index)).is_displayed

    def find_faq(self):
        faq_section = self.driver.find_element(By.CSS_SELECTOR, ".Home_FAQ__3uVm4")
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)
