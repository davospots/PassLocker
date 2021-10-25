import random
import string

import pyperclip


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

    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password

    def save_account(self):
        Credential.credential_list.append(self)

    def del_account(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_account(cls, account):

        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_account(cls):
        return cls.credential_list

    @classmethod
    def copy_account(cls, account):
        found_acc = Credential.find_account(account)
        pyperclip.copy(found_acc.password)

    @classmethod
    def find_by_acc(cls, account):
        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    def generate_pass(string_length =8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(string_length))