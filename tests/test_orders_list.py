import allure
from methods.order_methods import OrderMethods


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В ответе возвращается список заказов")
    def test_orders_list_return_orders(self):
        response = OrderMethods.get_orders_list()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
