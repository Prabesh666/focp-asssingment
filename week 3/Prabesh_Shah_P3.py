#1
name = input("Enter your name: ")

if name:
    print("Hello", name)
else:
    print("Hello, Stranger!")

#2
pw_1st = input("Enter your new password: ")

pw_2nd = input("Confirm your new password: ")

if pw_1st == pw_2nd:
    print("Password Set")
else:
    print("Error. Please try again.")

#3
pw_1st = input("Enter your new password: ")

if 8 <= len(pw_1st) <= 12:
    pw_2nd = input("Confirm your new password: ")
    
    if pw_1st ==   pw_2nd:
        print("Password Set")
        
    else:
        print("Error.Please try again.")
else:
    print("Password doesnt meet the criteria.")

#4
bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

pw_1st = input("Enter your new password: ")

if 8 <= len(pw_1st) <= 12:
    
    if pw_1st not in bad_passwords:
        pw_2nd = input("Confirm your new password: ")
        
        if pw_1st == pw_2nd:
            print("Password Set")
        else:
            print("Passwords do not match.Try again.")
            
    else:
        print("Weak password. Try using strong one.")
        
else:
    print("Password doesnt meet the criteri.")

#5
bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while (1):
    pw_1st = input("Enter your new password: ")

    if 8 <= len(pw_1st) <= 12:
        
        if pw_1st not in bad_passwords:
            
            pw_2nd = input("Confirm your new password: ")

            if pw_1st == pw_2nd:
                print("Password Set.")
                break 
            else:
                print("Passwords do not match.Try again.")
        else:
            print("Weak password.Try stronger one.")
    else:
        print("Password doesnt meet the criteria.")


#6
for i in range(1,11):
    seven_table = i * 7
    print(f"{seven_table} x 7 = {i}")

#7
table_of = int(input("Enter a number between 0 to 12: "))

if 1 <= table_of <= 12:
    for i in range(1,11):
        table = i * table_of
        print(f"{table_of} x {i} = {table}")
else:
    print("Please enter a valid number.")

#8
table_of = int(input("Enter a number: "))

if table_of >= 0:
    for i in range(1,11):
        table = i * table_of
        print(f"{table_of} x {i} = {table}")
else:
    table_of = -table_of
    for i in range(12, -1, -1):
        result = i * table_of
        print(f"{table_of} x {i} = {table}")
