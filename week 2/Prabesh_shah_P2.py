#1
user=input("Hello what is your name? ")
print(f"Hello {user}. Nice to meet you." )

#2
celsius = int(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}.C is equivalent to {fahrenheit}.F")

#3
Students = int(input("Number of Students : "))
req_size = int(input("Required group size :  "))
num_of_group = Students // req_size
rem_students = Students % req_size

if num_of_group == 1:
    group_word = "group"
else:
    group_word = "groups"

if rem_students == 0:
    print(f"There will be {num_of_group} {group_word}.")
else:
    print(f"There will be {num_of_group} {group_word} with {rem_students} student{'s' if rem_students > 1 else ''} left.")

# 4
tub_of_sweets = int(input("Enter total number of sweets: "))
pupils = int(input("Ente total number of pupils: "))
sweet_pupils = tub_of_sweets // pupils
leftover = tub_of_sweets % pupils
print(f"Each pupil will get {sweet_pupils} sweets, and there will be {leftover} sweets left over.")
