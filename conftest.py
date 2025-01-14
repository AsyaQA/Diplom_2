import pytest

from data import UserData
from methods.user import User


@pytest.fixture
def user():
    user = User()
    return user

@pytest.fixture
def authorized_user(user):
    new_user = UserData.USER_REGISTER
    user.create_user(new_user)
    login_user = user.login_user(new_user)
    yield {"Authorization": login_user.json()["accessToken"]}
    user.delete_user({"Authorization": login_user.json()["accessToken"]})
