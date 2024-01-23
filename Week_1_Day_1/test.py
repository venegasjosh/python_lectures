# #Strings

# first_name = "albert frank bob tyler"

# last_name = "einstein"

# username = "EINSTEINA"



# print("*********" +first_name.title() + "********")

# print(last_name.upper())

# print(username.lower())

# #remove white space

name = '     jordan went to the moon      '

# print(name)

# print(name.lstrip())

# print(name.rstrip())

# print(name.strip())

# #insert tabs
# message = "Grocery list:\n\tmilk\n\teggs"

# print(message)


# # Type Casting
# # example 1
# print("Hello" + 42)

# print("hello" + str(42))

# # example 2

# total = 35
# user_val = "26"
# # total = total + user_val
# total = total + int(user_val)

# print(total)


# # String Interpolation


# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# # Format

first_name = "Zen"
last_name = "Coder"
age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))






# # string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# # string.find(substring): returns the index of the start of the first occurrence of substring within string.
# # string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.


# # string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.


# # string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.




# #Numbers

# #random
import math
import random

# x = 1
# y= 100
# print(random.randint(x,y))


# print(math.sqrt(9))

# PI = math.pi

# print(PI)


# print(round(3.1415926,2))

# print(round(1234, -2))


# print(abs(-5))

# print(2 + 3)

# print(2 * 3)


# #Math with float numbers

# print(2.0 + 3)

# print(2.0 * 3)

# print(10/5)

# #Raising to the power of

# print(2**3)

# #Use parenthese to force a nonstandard order of operations

# print((2 + 3) * 4)


# #Booleans


# is_hungry = True
# has_freckles = False


# if(is_hungry):
#   print("hungry")
# else:
#   print("falsy")
  
  
# # Lists

# vowels = ['e','i','o']
# print(vowels[0])

# print(vowels[-3])

# vowels.append('u')

# print(vowels)

# how to insert

# vowels.insert(0,'a')
# vowels.append('u')
# print(vowels)

# #modify a list using it's index

# vowels[-1] = 'y'

# print(vowels)

# #Removing from a list

# airports = ["ANC", "JNU", "SEA", "SIT", "SEA"]

# airports.remove('SEA')

# print(airports)

# # If an item appears more than once in the list, only it's first appearance is removed.

# #The del keyword deletes an item at a specific position in the list using it's index:

# airports = ["ANC", "JNU", "SEA", "SIT"]

# del airports[2]

# print(airports)

# #The pop() method removes and returns the last item in a list. The pop() method can also accep an index and will remove and return the item at that index:

# airports = ["ANC", "JNU", "SEA", "SIT"]

# airport = airports.pop()

# print(airport)

# airport = airports.pop(0)

# print(airport)

# #Slicing a list

# #A slice is port of a list that begins with the item at the first index specified and stops with the item before the last index specified:

# states = ['CA', 'CO', "CT","DE","FL",  "GA"]

# print(states[2:4])

# print(states)

# #Omit the first index, and the slice starts with the first item in the list:

# print(states[:2])

# #Omit the second index and the slice goes to the end of the list:

# print(states[3:])

# # Copying a list

# states=['ca', 'co', 'ct', 'de']

# my_states = states[:]

# #Changes you make to the new list doesn't affect the original list:

# my_states.append("HI")

# print(my_states)

# print(states)

# Dictionaries

cars = {
  "ford": "bronco",
  "hyundia": "elantra",
  "volkswagon": ["bug", "van"]
}

# cars['volkswagon'] = 'van'

# print(cars['volkswagon'][1])

# companies = [
#   {
#   "ford": "bronco",
#   "hyundia": "elantra",
#   "volkswagon": ["bug", "van"]
#   },
  
#   {"clorox": "wipes"}
# ]



# #Use a for loop to loop through items in a list

countries = ["canada", 'usa', 'mexico']

# for country in countries:
#   print(f"I'm flying to {country}.")
  
#   #loop through part of a list using a slice:
  
# for country in countries[-1:]:
#   print(f"I've been to {country}")
  
  
# #sorting a list 

vowels = ['a,','i','u','e']

# print(sorted(vowels))

# vowels.sort()

# print(vowels)


# nums = [1,3,5,2]

# print(sorted(nums))


# #reversing a list

# vowels.reverse()

# print(vowels)
# #Tuples

elementry_grades = (2,3,4)

for grade in elementry_grades:
  print("here's a grade")
  
elementry_grades[0] = 1

print(elementry_grades)

# #Conditional statements

#   if(true):
#     print("hello")