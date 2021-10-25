import unittest
from unittest import TestCase

from User import User
from User import Credential


class Test(unittest, TestCase):

    def setUp(self):
        self.new_user = User("davymats", "mizza123XYZ")

    def test_init(self):
        self.assertEqual(self.new_user.user_name, 'davymats')
        self.assertEqual(self.new_user.password, "mizza123XYZ")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_account = Credential('Instagram', 'David_Mathaga', '123psw')

    def test_init(self):
        self.assertEqual(self.new_account.account, 'Instagram')
        self.assertEqual(self.new_account.user_name, 'David_Mathaga')
        self.assertEqual(self.new_account.password, '123psw')

    def save_acc(self):
        self.new_account.save_account()
        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):
        Credential.credential_list = []

    def save_many_acc(self):
        self.new_account.save_account()
        test_acc = Credential('Facebook','makaupete','6qeq456')
        test_acc.save_account()
        self.assertEqual(len(Credential.credential_list),2)

    def delete_acc(self):
        self.new_account.save_account()
        test_acc = Credential('Facebook', 'makaupete', '6qeq456')
        test_acc.save_account()

        self.new_account.del_account()
        self.assertEqual(len(Credential.credential_list),1)

    def find_by_acc(self):
        self.new_account.save_account()
        test_acc = Credential('Facebook', 'makaupete', '6qeq456')
        test_acc.save_account()

        credential = Credential.find_by_acc('Facebook')
        self.assertEqual(credential.account,test_acc.account)

    def test_display_all(self):
        self.assertEqual(Credential.display_account(),Credential.credential_list)





if __name__ == "__main__":
    unittest.main()
