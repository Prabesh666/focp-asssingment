#1
def num_validator(number):
    return 0 <= number <= 100
    
value = int(input("Enter a value: "))
if num_validator(value):
    print("This value is within the condition.")
else:
    print("This value doesnt meet the condition.")

#2
def checker(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

user_value = input("Value: ")
uppercase_count, lowercase_count = checker(user_value)

print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")

#3
def greetings():
    name = input("Enter your name: ").capitalize()
    print(f"Hi, {name}")
greetings()

#4
def slicer(string_value):
    if len(string_value) > 1:
        return string_value[:-1]
    else:
        return string_value

user_value = input("Enter a string value: ")
output = slicer(user_value)
print(f"String after last character removed: {output}")

#5
def cel_Fah(celsius):

    return (celsius * 9/5) + 32

def Fah_cel(fahrenheit):
 
    return (fahrenheit - 32) * 5/9

temp_celsius = 28
fahrenheit_equivalent = cel_Fah(temp_celsius)
print(f"{temp_celsius} Celsius is equal to {fahrenheit_equivalent:.2f} Fahrenheit")

temp_Fah = 172
celsius_equivalent = Fah_cel(temp_Fah)
print(f"{temp_Fah} Fahrenheit is equal to {celsius_equivalent:.2f} Celsius")

#6
def Fah_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

Temp = input("Enter the temperature in Fahrenheit: ")

temperature, unit = float(Temp[:-1]), Temp[-1].upper()

if unit == 'F':
    cel_equiv = Fah_cel(temperature)
    print(f"The equivalent temperature in Celsius is: {cel_equiv:.2f}C")
else:
    print("Try Again!!!")

#7 
def cel_fah(celsius):
    return (celsius * 9/5) + 32
temperatures = []

for i in range(6):
    Temp = input(f"Enter temperature {i + 1} in Celsius : ")
    temperature, unit = float(Temp[:-1]), Temp[-1].upper()
    
    if unit == 'C':
        temperature = cel_fah(temperature)
    
    temperatures.append(temperature)

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)

print(f"Maximum temperature: {max_temp:.2f}")
print(f"Minimum temperature: {min_temp:.2f}")
print(f"Mean temperature: {mean_temp:.2f}")

#8
def cel_fah(celsius):
    return (celsius * 9/5) + 32

temperatures = []

while True:
    Temp = input("Enter a temperature in Celsius: ")

    if not Temp:
        break

    temperature, unit = float(Temp[:-1]), Temp[-1].upper()

    if unit == 'C':
        temperature = cel_fah(temperature)

    temperatures.append(temperature)

if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"Maximum temperature: {max_temp:.2f}")
    print(f"Minimum temperature: {min_temp:.2f}")
    print(f"Mean temperature: {mean_temp:.2f}")
else:
    print("Input a value.")

