#Defining a new string

phrase = "Hello World"
string_number = "1234"
long_string = '''This is a new String that spans across
some test
tree lines, even if you print it'''
whitespace_string = '''This is a string which also
spans across two lines
    but also maintains the whitespace'''

my_long_string = "Here's a string that I want to write but not display \
across multiple lines"

print(my_long_string)

"""
Exercises
"""

#Exercise: print a string that uses double quotation marks inside the string
print("This is some sort of test \"Test\"")

#Exercise: print a string that uses an apostrophe (single quote) inside the string
print("'This is some sprt of a 'test' with a single apostrophe'")

#Exercise: print a string that spans across multiple lines
print('''This is a strong
which spans across multiple
lines''')

#Exercise: print a one-line string that you have written out on multiple lines
print("This \
is a test")

"""
#String functions
"""

string1 = "Anant"
string2 = "Sangar"

print(string1+" "+string2)

string3 = "Abracadabra"

print("On position two of the string Abracadabra you will find the letter: "+string3[1])

flavour = "Strawberry"
print(len(flavour))


#Here we're saying that take characters starting 5th character going up (but not including the 10th)
print(flavour[5:10])
print(flavour[:4])
print(flavour[3:])


"""
Exercises
"""

#Exercise: Create a string and print its length using the len() function
my_string = "I am learning Python"
print("Len of my_string is:",len(my_string))

#Exercis: Create two strings, concatenate them (add them next to each other) and print the combination
#of the two strings

string5 = "Anant"
string6 = "Sangar"
print(string6+string5)

#Exercise: print the string “zing” by using subscripting and index numbers on the string “bazinga”
#to specify the correct range of characters

my_string1 = "bazinga"
print(my_string1[2:6])
