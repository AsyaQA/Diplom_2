import requests

from methods.order import Order
from urls import Urls


class User(Order):

    def create_user(self, user_data):
        new_user = requests.post(
            f"{Urls.BASE_URL}{Urls.USER_REGISTER}",
            json=user_data
        )
        return new_user

    def login_user(self, json_user):
        login_user = requests.post(
            f"{Urls.BASE_URL}{Urls.USER_LOGIN}",
            json=json_user
        )
        return login_user

    def change_user_data(self, json_user, data=None):
        change_data = requests.patch(
            f"{Urls.BASE_URL}{Urls.USER_DATA}",
            json=json_user,
            headers=data
        )
        return change_data

    def delete_user(self, jwt_token):
        requests.delete(
            f"{Urls.BASE_URL}{Urls.USER_DATA}",
            headers=jwt_token
        )
