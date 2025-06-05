from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, name, surname, address, metro_station, phone, date, comment):
        # Заполнение первой части формы
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(surname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']").click()
        self.driver.find_element(By.XPATH, f"//div[text()='{metro_station}']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

        # Заполнение второй части формы
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='* Когда привезти самокат']")))
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Когда привезти самокат']").send_keys(date)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Про аренду')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Срок аренды')]").click()
        self.driver.find_element(By.XPATH, "//div[text()='сутки']").click()
        self.driver.find_element(By.XPATH, "//input[@id='black']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']").send_keys(comment)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']").click()

    def confirm_order(self):
        self.driver.find_element(By.XPATH, "//button[text()='Да']").click()

    def check_success_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"))
        ).text