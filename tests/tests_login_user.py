import allure

from data import UserData


class TestsLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_user(self, user):
        response = user.login_user(UserData.USER_STATIC)
        assert "accessToken" in response.json()

    @allure.title('Логин с неверным логином и паролем')
    def test_without_created_login_user(self, user):
        response = user.login_user(UserData.USER_WITHOUT_NAME)
        assert "email or password are incorrect" in response.json()["message"]
