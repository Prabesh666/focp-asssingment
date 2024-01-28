from Password_Manager import add_user

filename = 'password.txt'

username = input("Enter New Username:- ")
real_name = input("Enter Real Name:- ")
password = input("Enter Password:- ")

add_user(username, real_name, password, filename)
