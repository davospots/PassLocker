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


def save_account(new_acc):
    new_acc.save_account()


def display_acc():
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

                break
            elif password_choice == 'gp':
                password = generate_password()

                break
            else:
                print('Invalid Password please try again')
        save_user(create_user(user_name, password))
        print('*' * 85)
        print(f'Hello {user_name}, Your account has been created successfully! Your Password is:{password}')
        print('*' * 85)
    elif the_code == 'li':
        print('*' * 50)
        print('Enter your username and password to login:')
        print('*' * 50)
        user_name = input('User Name: ')
        password = input('Password: ')
        login = login_user(user_name, password)
        if login == login_user:
            print(f'Hello{user_name}.Welcome Back')
            print('\n')
    while True:
        print('Use these Short Codes to proceed: \n CC - Create new Credential\n DC - Display Credentials \n FC -Find '
              'Credential \n D - Delete Credential \n EX - Exit \n')
        the_code = input().lower().strip()
        if the_code == 'cc':
            print('Create New Credential')
            print('.' * 20)

            account = input('Account Name : ').lower()
            user_name = input('User Name : ')
            while True:
                print('TP - To type your own password if you already have an account:\n GP - To generate random '
                      'Password')
                password_choice = input().lower().strip()
                if password_choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")

            save_account(make_acc(account, user_name, password))
            print('\n')
            print(f'Account: {account} Username: {user_name} Password: {password} created successfully ')
            print('\n')
        elif the_code == 'dc':
            if display_acc():
                print("Here's your list of accounts:")
                for account in display_acc():
                    print(f'Account:{account}\n UserName:{user_name}\n Password:{password}')
            else:
                print('You have no saved accounts')
        elif the_code == 'fc':

            search_acc = input('Enter the account you are looking for: ').lower()

            if find_credential(search_acc):
                print(f'Account Name: {account}')
                print(f'User Name: {user_name}')
                print(f'Password: {password}')

        elif the_code == 'd':
            print('Which account do you want to delete?')
            search_acc = input().lower()
            if find_credential(search_acc):
                search_acc = find_credential(search_acc)
                print('_' * 50)
                search_acc.del_account()
                print('\n')
                print(f'the credentials for : {account} has been deleted')
        elif the_code == 'ex':
            print(f'Goodbye {user_name}')
            break

    else:
        print('Please enter valid input')


pass_locker()
