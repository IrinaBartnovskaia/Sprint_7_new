import pytest
import allure

from methods.order_methods import OrderMethods


@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Можно создать заказ с разными вариантами цвета")
    def test_create_order_return_track(self, color):
        order_body = {
            "firstName": "Irina",
            "lastName": "Bart",
            "address": "Moscow, Red Square 1",
            "metroStation": 4,
            "phone": "+79035553535",
            "rentTime": 5,
            "deliveryDate": "2026-01-05",
            "comment": "test order",
            "color": color
        }

        response = OrderMethods.create_order(order_body)

        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] is not None
