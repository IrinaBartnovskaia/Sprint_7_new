import pytest
import allure
import requests

from generators import generate_fake_courier
from methods.courier_methods import CourierMethods
from data import Message, URL


@allure.feature('Логин курьера')
class TestCourierLogin:

    @allure.title('Курьер может авторизоваться и возвращается id')
    def test_courier_can_login_and_return_id(self, create_and_delete_courier):
        login, password = create_and_delete_courier

        response = CourierMethods.login_courier(login, password)

        assert response.status_code == 200
        assert response.json().get('id') is not None

    @pytest.mark.parametrize('field', ['login', 'password'])
    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_missing_required_field_error(self, create_and_delete_courier, field):
        login, password = create_and_delete_courier

        body = {"login": login, "password": password}
        del body[field]

        response = requests.post(URL.LOGIN_COURIER_URL, json=body)

        assert response.status_code == 400

        if response.status_code == 400:
            assert response.json().get('message') == Message.LOGIN_COURIER_MISSING_FIELDS
    @allure.title('Ошибка, если неправильно указать логин или пароль')
    def test_login_with_wrong_credentials_error(self, create_and_delete_courier):
        login, password = create_and_delete_courier

        response = CourierMethods.login_courier(login, password + "wrong")

        assert response.status_code == 404
        # имя константы подставь то, которое у тебя реально в Message
        assert response.json().get('message') == Message.LOGIN_COURIER_NOT_FOUND

    @allure.title('Ошибка, если авторизоваться под несуществующим пользователем')
    def test_login_nonexistent_user_error(self):
        response = CourierMethods.login_courier("no_such_login_123", "no_such_pass_123")

        assert response.status_code == 404
        # имя константы подставь то, которое у тебя реально в Message
        assert response.json().get('message') == Message.LOGIN_COURIER_NOT_FOUND
