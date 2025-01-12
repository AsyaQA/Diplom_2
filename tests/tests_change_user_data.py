import allure
import pytest

from data import UserData


class TestsChangeUser:

    @allure.title('Изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize(
        "json_user",
        [
            UserData.CHANGE_EMAIL,
            UserData.CHANGE_PASSWORD,
            UserData.CHANGE_NAME
        ]
    )
    def test_change_user_data_authorized(self, user, authorized_user, json_user):
        response = user.change_user_data(json_user, authorized_user)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize(
        "json_user",
        [
            UserData.CHANGE_EMAIL,
            UserData.CHANGE_PASSWORD,
            UserData.CHANGE_NAME
        ]
    )
    def test_change_user_data_without_authorized(self, user, json_user):
        response = user.change_user_data(json_user)
        assert response.status_code == 401 and response.json()["success"] == False
