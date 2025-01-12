import allure
import pytest

from data import UserData


class TestsUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, user):
        response = user.create_user(UserData.USER_REGISTER)
        assert "accessToken" in response.json()

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_who_is_already_registered(self, user):
        response = user.create_user(UserData.USER_STATIC)
        assert "User already exists" in response.json()["message"]

    @allure.title('Создание пользователя и не заполнение одного из обязательных полей')
    @pytest.mark.parametrize(
        "data",
        [
            UserData.USER_WITHOUT_EMAIL,
            UserData.USER_WITHOUT_PASSWORD,
            UserData.USER_WITHOUT_NAME
        ]
    )
    def test_create_user_without_one_some_params(self, user, data):
        response = user.create_user(data)
        assert "Email, password and name are required fields" in response.json()["message"]
