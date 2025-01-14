import allure
import pytest

from data import UserData, MessageData


class TestsUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, user):
        response = user.create_user(UserData.USER_REGISTER)
        assert "accessToken" in response.json() and response.status_code == 200

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_who_is_already_registered(self, user):
        response = user.create_user(UserData.USER_STATIC)
        assert MessageData.MESSAGE_ALREADY_REGISTERED in response.json()["message"] and response.status_code == 403

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
        assert MessageData.MESSAGE_WITHOUT_ONE_SOME_PARAMS in response.json()["message"] and response.status_code == 403
