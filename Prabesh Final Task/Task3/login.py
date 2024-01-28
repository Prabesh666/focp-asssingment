
from Password_Manager import login

filename = 'password.txt'

username = input("User_Name:- ")
password = input("Password:- ")

login(username, password, filename)
