from __future__ import division

"""
Assignment
Write a script exponent.py that receives two numbers from the user and displays the result
of taking the first number to the power of the second number. A sample run of the program
should look like this (with example input that has been provided by the user included below):
1 >>>
2 Enter a base: 1.2
3 Enter an exponent: 3
4 1.2 to the power of 3 = 1.728
5 >>>
"""

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")
print("{} to the power of {} is {}".format(base,exponent,float(base)**float(exponent)))

"""
Functions
"""

#Function for Square
def square1(base):
    return base**2

print(square1(4))

#Function for difference
def minus(num1, num2):
    return num1 - num2

print(minus(2,1))


"""
Excersise

1. Write a cube() function that takes a number and multiplies that number by itself twice
over, returning the new value; test the function by displaying the result of calling your
cube() function on a few different numbers
"""

def cube(number):
    return number*number

print(cube(3))


"""
Excersise
2. Write a function multiply() that takes two numbers as inputs and multiplies them
together, returning the result; test your function by saving the result of multiply(2,
5) in a new integer object and printing that integer’s value
"""

def multiply(num1, num2):
    output = num1 * num2
    return output

output = multiply(2,4)
print(output)


"""
Write a script temperature.py that includes two functions. One function takes a Celsius temperature
as its input, converts that number into the equivalent Fahrenheit temperature and
returns that value. The second function takes a Fahrenheit temperature and returns the
equivalent Celsius temperature. Test your functions by passing input values to them and
printing the output results.
For testing your functions, example output should look like:
1 72 degrees F = 22.2222222222 degrees C
2 37 degrees C = 98.6 degrees F
"""

def FahrenheitToCelcius(number):
    celcius = (number-32)*5/9
    print("{} degrees F = {} degrees C".format(number,celcius))

FahrenheitToCelcius(72)

def CelsiusToFahrenheit(number):
    fahrenheit = number * 9/5 +32
    print("{} degrees C = {} degrees F".format(number,fahrenheit))

CelsiusToFahrenheit(37)



"""
Loops
"""

#While Loops

n = 1
while (n < 10):
    print(n)
    n = n + 1

for n in range(1,9):
    print(n)

for n in range(1,4):
    for j in ["a","b","c"]:
        print(n,j)


"""
1. Write a for loop that prints out the integers 2 through 10, each on a new line, by using
the range() function
"""

print("Excercises")
for i in range(2,11):
    print(i)


"""
2. Use a while loop that prints out the integers 2 through 10 (Hint: you’ll need to create
a new integer first; there’s no good reason to use a while loop instead of a for loop in
this case, but it’s good practice…)
"""

n = 2
while(n<11):
    print(n)
    n = n + 1

"""
3. Write a function doubles() that takes one number as its input and doubles that number
three times using a loop, displaying each result on a separate line; test your function
by calling doubles(2) to display 4, 8, and 16
"""

print("Last Excercise")
def doubles(num1):
    for i in range(1,4):
        num1 = num1 * 2
        print(num1)

print(doubles(2))


"""
Assignment: Track your investments
Write a script invest.py that will track the growing amount of an investment over time. This
script includes an invest() function that takes three inputs: the initial investment amount,
the annual compounding rate, and the total number of years to invest. So, the first line of the
function will look like this:
1 def invest(amount, rate, time):
The function then prints out the amount of the investment for every year of the time period.
In the main body of the script (after defining the function), use the following code to test your
function: invest(100, .05, 8)
Running this test code should produce the following output exactly:
1 principal amount: $100
2 annual rate of return: 0.05
3 year 1: $105.0
4 year 2: $110.25
5 year 3: $115.7625
6 year 4: $121.550625
7 year 5: $127.62815625
8 year 6: $134.009564063
9 year 7: $140.710042266
10 year 8: $147.745544379
11 principal amount: $2000
12 annual rate of return: 0.025
13 year 1: $2050.0
14 year 2: $2101.25
15 year 3: $2153.78125
16 year 4: $2207.62578125
17 year 5: $2262.81642578
"""

def invest(amount, rate, time):
    print("principal amount is: ",amount)
    print("annual rate of return: ", rate)

    for year in range(0,time):
        amount = amount * (1+(rate/100))
        print("year {}: {}".format(year+1,amount))

invest(100,5,8)


"""
Write a function which adds underscores in a word
"""

def add_underscore(word):
    u_word = ""
    for i in range(0, len(word)):
        u_word = u_word + word[i] + "_"

    print(u_word)

add_underscore("hallo")
