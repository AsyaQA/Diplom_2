import requests
from urls import Urls


class Order:

    def create_order(self, json_order, data=None):
        new_order = requests.post(
            f"{Urls.BASE_URL}{Urls.ORDER}",
            json=json_order,
            headers=data
        )
        return new_order

    def get_user_orders(self, data=None):
        orders = requests.get(
            f"{Urls.BASE_URL}{Urls.ORDER}",
            headers=data
        )
        return orders
