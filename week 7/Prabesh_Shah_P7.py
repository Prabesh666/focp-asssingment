#1
# Using a set comprehension to extract unique letters from an input string s while leaving 
# aside non-alphabetic characters. The sorted() method then guarantees that the letters are 
# ordered alphabetically.
def get_unique_letters(s):
    return sorted(set(s.lower() for s in s if s.isalpha()))
print(get_unique_letters('cheese')) # Output: ['c', 'e', 'h', 's']
print(get_unique_letters('PythonProgramming')) # Output: ['g', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y']
print(get_unique_letters('HelloWorld')) # Output: ['d', 'e', 'h', 'l', 'o', 'r', 'w']
print(get_unique_letters('Able was I ere I saw Elba')) # Output: ['a', 'b', 'e', 'i', 'l', 's', 'w']

# The s.isalpha() method in Python checks whether the string 's' consists of alphabetic characters only. 
# If all characters in the string are alphabets, then it returns True, otherwise False. 

#2
def union_letters(word1, word2):
    #union
    return sorted(set(word1) | set(word2))

def intersection_letters(word1, word2):
    #intersection
    return sorted(set(word1) & set(word2))

def sym_difference_letters(word1, word2):
    #symmetric difference
    return sorted(set(word1) ^ set(word2))
print(union_letters("prasi","josi"))  
print(intersection_letters('Hello', 'duniya'))
print(sym_difference_letters('sun', 'shine'))  
# ['a', 'i', 'j', 'o', 'p', 'r', 's']
# []
# ['e', 'h', 'i', 'u']

#3
dict_of_capitals = {'Nepal': 'Kathmandu', 'India': 'Delhi', 'United Kingdom': 'London'}

while True:
    country = input("Country name: ").title()
    if country in dict_of_capitals:
        print("The capital city of", country, "is",dict_of_capitals[country])
    else:
        capital = input("We don't know the capital city. Please enter it: ")
        dict_of_capitals[country] = capital
# Country name: Nepal
# The capital city of Nepal is Kathmandu
# Country name: USA
# We don't know the capital city. Please enter it: APPLE
# Country name: USA
# The capital city of Usa is APPLE





