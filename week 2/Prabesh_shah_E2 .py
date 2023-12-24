Variables and Types
Exercises
Week 2

Which is the purpose of a variable within Python?
Answer: To store data and retrieve that data using some name.

Write a simple Python statement that creates and assigns a value of 3.142 to a variable called ‘pi’
Answer:
pi = 3.142
print(pi)

Which of the following is NOT a valid name for a variable within Python?
total result question? name_1
Answer: Question? Isn’t a valid name as it contains special characters.

Following the execution of the code below, what will be stored in the variable 'age'?
age = 10 + 20
age = age + 5 
Answer: The value stored would be 35


In the answer box below write the exact output that would be displayed if the following statement was executed (assuming age has been created as in the previous question):
print("The age value is",age)
The age value is 35

Which of the following is an example of an Augmented Assignment in Python?
total = 20
total = total +5 total *= 100 total  = max
Answer:
The line total *= 100 is the augmented assignment.

Which of the following is an example of an integer type variable?
result = "xyz" result = 20 result = 20.5 result = False 
Answer:
The result = 20 is an  example of integer type variable

_________________________________________________________________________
What are the only two legal values of a boolean type variable?
Answer:
0 and 1 

Following the execution of the code below, what will be the data-type of the variable 'average'?
average = total / count 
Answer: Float

Following the execution of the code below, what will be the data-type of the variable 'message'? message = "hello there!"
 Answer: It will be string.

What determines the current data-type of a variable?
Answer: The value it holds.

What is the purpose of the built-in type() function?
Answer: It’s purpose is to find the data type of the variable assigned.

What would be the output following execution of the following code?
type(10.2) 
Answer:
It would be a float.

Does the Python language support Dynamic Typing, or Static Typing?
Answer:
It supports Dynamic Typing.

Which of the following is an example of a function call?
answer = 10 
print(answer) 
total *= 10 
10 + 20
 
Answer: Print(answer) is a function call.

What is the name given to the values that are passed to a function within the parentheses?
Answer: Parameters or arguements
 
What is the purpose of the built-in input() function?
Answer: Its purpose is to take input values from the user.
 
What is the data-type of the value returned by the input() function?
Answer:String
 
Use the Python interpreter to input a small Python program that prints your name and address on the screen. Once this works type the program in the answer box below.
Answer:
print("My name is Prashiddha Joshi")
print("I live in Bajrabarahi,Godawari,Lalitpur")
 
Within the answer box below write a small Python program, that when run, would print the following message including the double quotes -
Hello, is your name "Bwian"?
Answer:print('Hello, is your name "Bwian"?')
 
Now write a second small Python program, that when run, would print the following message including the single quotes -
Or is your name 'Woger'?
Answer:print("Or is your name 'Woger'?")
 
Within the answer box below write a small Python program, that when run, uses escape sequences to print the following text exactly.
This is a string containing a backslash (\),     a single quote ('), a double quote (")     and is split across multiple lines
print("This is a string containing a backslash (\),\n\t a single quote ('), a double quote (\")\n\t and is split across multiple lines")

Within the answer box below write a small Python program, that when run, uses triple quotes to print the following text exactly.
This is a string containing a backslash (\),     a single quote ('), a double quote (")     and is split across multiple lines 
Answer: 
print("""
This is a string containing a backslash (\\),
     a single quote ('), a double quote (\")
     and is split across multiple lines
""")

Use the Python interpreter to input a small Python program that asks the user to input a temperature in fahrenheit. Once the value has been input, display a message that shows the same temperature in celsius. You may have to do some research in order to find out the conversion method. Once this works, type the program in the answer box below.
Answer:
Temperature=input(“Enter the temperature in fahrenheit:”)
celsius = (fahrenheit - 32) * 5/9
print(“The temperature fahrenheit”, fahrenheit “in celsius is:”,celsius)


Within the answer box below write a small Python program that asks the user to enter two values. Store these in variables called 'a' and 'b' respectively.
Answer:
a=int(input(“Enter a value:”))
b=int(input(“Enter a value:”))

Once the values have been input use three calls to the print() function to show output such as the following (in this example the user entered 10.2 and 18.3) -
The value 'a' was 10.2 and the value 'b' was 18.3
The sum of 'a' and 'b' is 28.5 The product of 'a' and 'b' is 186.66 Answer:
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
print("The value a was:",a)
print("The value b was:",b)
print("The sum of a and b is:",a+b)
print("The product of a and b is:",a*b)

Python includes a built-in function called max(). When this is called with multiple argument values it returns the largest of the given arguments. e.g.
max(20, 50, 30)  # this would return 50
Within the answer box below write a small program that asks the user to input three values. Store these in variables (the names are up to you) then use the max() function to display the largest of the input values.
Answer:
num1 = int(input("Enter any value: "))
num2 = int(input("Enter any value: "))
num3 = int(input("Enter any value: "))
largest_num = max(num1, num2, num3)
print("The largest value entered is:", largest_num)

 
Using the Python interpreter execute your code, then examine the output generated when the input the values are 'hello', 'welcome', and 'bye'
Does the program still show the maximum value? If not, what does it show?
Answer:No the max() function doesnt determine the largest among the string values.
 
 
Given the following definition:
name = "Black Knight"
What would each of the following Python statements display?

print( name[0] ) Answer:B
print( name[4] ) Answer: K
print( name[-1] ) Answer:T
print( name[-2] ) Answer:H
print( name[2:5] ) Answer:ACK
print( name[6:] ) Answer:KNIGHT
print( name[:5] ) Answer:BLACK
print( name[:] )  Answer:BLACK KNIGHT
 
Which of the following creates a variable containing a List?
names = "Terry" 
names = 10 
names = [ "Mark", "Jon", "Amanda", "Edward", "Sally" ] names = "Mark", "Jon", "Amanda"]
Answer: This one is the list names = [ "Mark", "Jon", "Amanda", "Edward", "Sally" ] names = "Mark", "Jon", "Amanda"]

 
Is the following a valid List, even though it contains values based on different data-types?
values = [10.2, "Jon", False, "Edward", True ] 
Answer: Yes it is a list as list supports every data types.
 
If a value is mutable, can it be modified after it has been created?
Answer: Yes if it is mutable it can be modified like list.
 
What term is used to describe a value that cannot be changed once it has been created?
Answer: Immutable values
 
Is a List mutable or immutable?
Answer: It is mutable.
 
Is a String mutable or immutable?
Answer: It is immutable.

Given the following definition -
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
What would each of the following Python statements display?
print( names[2] ) 
Answer: Micheal
 
print( names[-2] )
Answer:Terry
 
print( names[0:3] ) 
Answer:['Terry', 'John', 'Michael']
 
names = names + "Brian" 
print( names )
Answer: Cant concanate a string with list.
 
names[0:1] = ["Mark", "Jon"] print( names ) 
Answer:['Mark', 'Jon', 'John', 'Michael', 'Eric', 'Terry', 'Graham']
 
What built-in function within Python can be used to find out how many elements are contained within a string or list?
Answer:len() function can be used to find out how many elemets are contained.
 

