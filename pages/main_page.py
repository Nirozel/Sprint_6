from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self):
        cookie_button = (By.XPATH, "//button[@id='rcc-confirm-button']")
        self.wait.until(EC.element_to_be_clickable(cookie_button)).click()

    def click_order_button_header(self):
        order_button = (By.XPATH, "//button[contains(text(), 'Заказать')][@class='Button_Button__ra12g']")
        self.wait.until(EC.element_to_be_clickable(order_button)).click()

    def click_order_button_footer(self):
        order_button = (By.XPATH, "//button[contains(text(), 'Заказать')][@class='Button_Button__ra12g Button_Middle__1CSJM']")
        self.wait.until(EC.element_to_be_clickable(order_button)).click()

    def click_scooter_logo(self):
        logo = (By.XPATH, "//img[@alt='Scooter']")
        self.wait.until(EC.element_to_be_clickable(logo)).click()

    def click_yandex_logo(self):
        logo = (By.XPATH, "//img[@alt='Yandex']")
        self.wait.until(EC.element_to_be_clickable(logo)).click()

    def find_faq(self):
        faq_section = self.driver.find_element(By.CSS_SELECTOR, ".Home_FAQ__3uVm4")
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)