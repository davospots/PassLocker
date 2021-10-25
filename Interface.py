#! /usr/bin/env python3.10

from User import User, Credential


def create_user(user_name, password):
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    user.save_user()


def display_user():
    return User.display_user()


def login_user(user_name, password):
    check_user = Credential.verify_user(user_name, password)
    return check_user


def make_acc(account, user_name, password):
    new_acc = Credential(account, user_name, password)
    return new_acc


def save_acc(credentials):
    credentials.save_account()


def display_acc_details():
    return Credential.display_account()


def delete_acc(credentials):
    credentials.del_account()


def find_credential(account):
    return Credential.find_by_acc(account)


def generate_password():
    gen_pass = Credential.generate_password()
    return gen_pass


def pass_locker():
    print("Hi,please enter one of the following to proceed.\n CA --- Create New Account\n LI --- Have An Account")
    the_code = input('').lower().strip()
    if the_code == 'ca':
        print('Sign Up')
        print('*' * 50)
        user_name = input('User_name : ')
        while True:
            print("TP - To type your own password:\n GP - To generate Password")
            password_choice = input().lower().strip()
            if password_choice == 'tp':
                password = input('Enter Password\n')
                print(password)
                break
            elif password_choice == 'gp':
                password = generate_password()
                print(password)
                break
            else:
                print('Invalid Password please try again')


pass_locker()
