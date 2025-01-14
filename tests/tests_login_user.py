import allure

from data import UserData, MessageData


class TestsLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_user(self, user):
        response = user.login_user(UserData.USER_STATIC)
        assert "accessToken" in response.json() and response.status_code == 200

    @allure.title('Логин с неверным логином и паролем')
    def test_without_created_login_user(self, user):
        response = user.login_user(UserData.USER_WITHOUT_NAME)
        assert MessageData.MESSAGE_INCORRECT in response.json()["message"] and response.status_code == 401
