import helpers


class UserData:

    USER_REGISTER = helpers.get_register_params()
    USER_STATIC = {
        "email": "JCv161@mail.com",
        "password": "h2467o",
        "name": "XKXYGR"
    }
    USER_WITHOUT_EMAIL = {
        "password": helpers.random_password(),
        "name": helpers.random_name()
    }
    USER_WITHOUT_PASSWORD = {
        "email": helpers.random_email(),
        "name": helpers.random_name()
    }
    USER_WITHOUT_NAME = {
        "email": helpers.random_email(),
        "password": helpers.random_password()
    }
    CHANGE_EMAIL = {"email": helpers.random_email()}
    CHANGE_PASSWORD = {"password": helpers.random_password()}
    CHANGE_NAME = {"name": helpers.random_name()}

class OrderData:

    ALL_INGREDIENTS = {"ingredients": helpers.get_list_id_ingredients()}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INVALID_INGREDIENTS = {"ingredients": ["61c0c5a71d", "61c0c5a71d"]}

class MessageData:

    MESSAGE_WITHOUT_ONE_SOME_PARAMS = "Email, password and name are required fields"
    MESSAGE_ALREADY_REGISTERED = "User already exists"
    MESSAGE_INCORRECT = "email or password are incorrect"
