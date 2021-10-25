import random
import string


class User:
    user_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)


class Credential:
    credential_list = []

    @classmethod
    def verify_user(cls, user_name, password):

        current_user = ''
        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                current_user == user.user_name
            return current_user
