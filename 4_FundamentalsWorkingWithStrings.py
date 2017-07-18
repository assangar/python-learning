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
