import requests
import allure
from data import URL


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body):
        return requests.post(URL.CREATE_ORDER_URL, json=body)
    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders_list():
        return requests.get(URL.GET_ORDERS_URL)
