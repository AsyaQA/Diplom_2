import allure

from data import OrderData


class TestsOrder:

    @allure.title('Создание заказа с авторизацией и ингридиентами')
    def test_create_order_authorized(self, user, authorized_user):
        response = user.create_order(OrderData.ALL_INGREDIENTS, authorized_user)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorized(self, user):
        response = user.create_order(OrderData.ALL_INGREDIENTS)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Создание заказа без ингридиентов')
    def test_create_order_without_ingredients(self, user):
        response = user.create_order(OrderData.WITHOUT_INGREDIENTS)
        assert response.status_code == 400 and response.json()["success"] == False

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredients(self, user):
        response = user.create_order(OrderData.INVALID_INGREDIENTS)
        assert response.status_code == 500

    @allure.title('Получение заказа авторизированного пользователя')
    def test_get_orders_authorized_user(self, user, authorized_user):
        response = user.get_user_orders(authorized_user)
        assert response.status_code == 200 and "orders" in response.json()

    @allure.title('Получение заказа неавторизированного пользователя')
    def test_get_orders_without_authorized_user(self, user):
        response = user.get_user_orders()
        assert response.status_code == 401 and response.json()["success"] == False
