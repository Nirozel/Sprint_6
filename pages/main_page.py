from .base_page import BasePage
from locators.locators_main import MainPageLocators


class MainPage(BasePage):
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.questions_section)
