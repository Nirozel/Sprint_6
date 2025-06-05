import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @pytest.mark.parametrize("order_button, user_data", [
        ("header", {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, ул. Ленина, 1",
            "metro_station": "Черкизовская",
            "phone": "+79991234567",
            "date": "01.01.2025",
            "comment": "Тестовый заказ"
        }),
        ("footer", {
            "name": "Петр",
            "surname": "Петров",
            "address": "Санкт-Петербург, Невский пр., 10",
            "metro_station": "Сокольники",
            "phone": "+79997654321",
            "date": "02.01.2025",
            "comment": "Второй тестовый заказ"
        })
    ])
    def test_order_flow(self, driver, order_button, user_data):
        main_page = MainPage(driver)
        main_page.open()

        if order_button == "header":
            main_page.click_order_button_header()
        else:
            main_page.click_order_button_footer()

        order_page = OrderPage(driver)
        order_page.fill_order_form(**user_data)
        order_page.confirm_order()
        assert "Заказ оформлен" in order_page.check_success_message()