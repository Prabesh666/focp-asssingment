
from Password_Manager import change_password

filename = 'password.txt'

username = input("User: ")
current_password = input("Current Password: ")
new_password = input("New Password: ")
confirm_password = input("Confirm: ")

if new_password == confirm_password:
    change_password(username, current_password, new_password, filename)
else:
    print("Passwords do not match. Nothing changed.")
