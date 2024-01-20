#1
names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)
#The name wont be repeated or shown after using print() as set doesnt allow repeated values.

#2
sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
#{'i', ' ', 'e', 'h', 'a', 'r', 'c', 's', 'l', 'n', 'g', 'd', 'o', 't', 'u', 't', 'p', 'm', 'b', 'y', 'v', 'w', 'z', 'f', 'q', 'j', 'k', 'x'}

#3
names = {"John", "Jane", "Sam", "Jill"}

name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names")
else:
    print("You are listed in the set of known names")
# Enter your name: prashiddha
# You are not listed in the set of known names

#4
help(set)
# Help on class set in module builtins:
# class set(object)
#  |  set() -> new empty set object
#  |  set(iterable) -> new set object
#  |
#  |  Build an unordered collection of unique elements.
#  |
#  |  Methods defined here:
#  |
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |
#  |  __contains__(...)
#  |      x.__contains__(y) <==> y in x.
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __iand__(self, value,/)

#5
staff = {"Paul", "John", "George"}
directors = {"Michael", "Sir George Martin"}

staff = staff.union({"Mark", "Ringo"})
print(staff)

inter_section= staff.intersection(directors)
print(inter_section)

diff_erence = staff.difference(directors)
print(diff_erence)

sym_difference = staff.symmetric_difference(directors)
print(sym_difference)

# {'Paul', 'Mark', 'Ringo', 'George', 'John'}
# set()
# {'Mark', 'Paul', 'John', 'George', 'Ringo'}
# {'Mark', 'Michael', 'Paul', 'John', 'Sir George Martin', 'George', 'Ringo'}

#6
vowels = set({"a", "e", "i"})
vowels.update({"o", "u"})
print(vowels)
# {'e', 'i', 'a', 'u', 'o'}

#7
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("All managers are staff members")
# All managers are staff members
# All managers are staff members

#8
help(frozenset)

# class frozenset(object)
#  |  frozenset() -> empty frozenset object
#  |  frozenset(iterable) -> frozenset object
#  |
#  |  Build an immutable unordered collection of unique elements.
#  |
#  |  Methods defined here:
#  |
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |
#  |  __contains__(...)
#  |      x.__contains__(y) <==> y in x.
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)

#9
 import math
 roots = {n : math.sqrt(n) for n in range(1,26)}
 print(roots)
# {1: 1.0, 2: 1.4142135623730951, 3: 1.7320508075688772, 4: 2.0, 
#  5: 2.23606797749979, 6: 2.449489742783178, 7: 2.6457513110645907, 
#  8: 2.8284271247461903, 9: 3.0, 10: 3.1622776601683795, 11: 3.3166247903554, 
#  12: 3.4641016151377544, 13: 3.605551275463989, 14: 3.7416573867739413,
#  15: 3.872983346207417, 16: 4.0, 17: 4.123105625617661, 18: 4.242640687119285,
#  19: 4.358898943540674, 20: 4.47213595499958, 21: 4.58257569495584, 
#  22: 4.69041575982343, 23: 4.795831523312719, 24: 4.898979485566356, 25: 5.0}

#10
stock = {'apple': 1, 'banana': 4, 'cherry': 9}
stock['kiwi'] = 10
print(stock)
# {'apple': 1, 'banana': 4, 'cherry': 9, 'kiwi': 10}

#11
help(dict)
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).

stock = {'apple': 1, 'banana': 4, 'cherry': 9, 'kiwi': 10}
popped_items = stock.popitem() 
print(popped_items)
print(stock)
# ('kiwi', 10)
# {'apple': 1, 'banana': 4, 'cherry': 9}


#12
roots = {4: 2, 9: 3, 16: 4, 25: 5}
for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")
# The square root of 4 is 2
# The square root of 9 is 3
# The square root of 16 is 4
# The square root of 25 is 5

#13
Set: An unordered collection of unique elements.
Set Operations: Manipulations like union, intersection, and difference on sets.
Set Comprehension: Creating sets using a concise and expressive syntax based on a condition.
Dictionary: A collection of key:value pairs, providing an efficient way to store and retrieve data.
Key:Value Pair: The fundamental components of a dictionary, where a key serves as an identifier for its associated value.