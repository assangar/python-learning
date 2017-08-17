string1 = "2"
string2 = "3"

print(string1 + string2)
print(string1*3)

"Casting"
"You can cast different object into other object types"

#Casting String into Int
my_number = "12"
print(my_number*3)
i = int(my_number)
print(i*3)

#Casting Int into String
my_number1 = 12
print(my_number1*3)
i = str(my_number1)
print(i*3)


"Excercise"
"""
1.Create a string object that stores an integer as its value, then convert that string into
an actual integer object using int(); test that your new object is really a number by
multiplying it by another number and displaying the result
"""
print("Excersise 1")
my_number = "12"
print(my_number*3)
i = int(my_number)
print(i*3)


"""
2. Repeat the previous exercise, but use a floating-point number and float()
"""
print("Excersise 2")
my_number = "12"
i = float(my_number)
print(i*3)

"""
3. Create a string object and an integer object, then display them side-by-side with a single
print statement by using the str() function
"""
print("Excersise 3")
my_string = "Hallo this is a test"
my_int = 12
print(my_string+str(my_int))


"""
Streamlining the print statement
"""

name = "Anant Sangar"

num_heads = 2
num_arms = 3

print("The number",num_heads," the second number is", num_arms)
print("The number {} the second number is {}".format(num_arms,num_heads))

#page 43


"""
Find Strings
"""

my_string = "Hallo this is a test"
print(my_string.find("is"))

"""
Exercises
"""

"""
In one line, display the result of trying to find() the substring a in the string AAA
the result should be -1
"""

print("AAA".find("A"))

"""
2. Create a string object that contains the value "version 2.0" find() the first occurrence
of the number 2.0 inside of this string by first creating a "float" object that stores the
value 2.0 as a floating-point number, then converting that object to a string using the
str() function
"""


test_string = "version 2.0"

print("test_string")
number = float(test_string[test_string.find("2.0")])
print(number)


my_string = "version 2.0"
my_float = float(my_string[my_string.find("2.0")])
print("This is the extracted number: ", my_float)

"""
3. Write and test a script that accepts user input using raw_input(), then displays the
result of trying to find() a particular letter in that input
"""

