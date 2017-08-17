"""
Write a script translate.py that asks the user for some input with the following prompt:
Enter some text:
You should then use the replace() method to convert the text entered by the user into
    leetspeak by making the following changes to lower-case letters:
The letter: a becomes: 4
The letter: b becomes: 8
The letter: e becomes: 3
The letter: l becomes: 1
The letter: o becomes: 0
The letter: s becomes: 5
The letter: t becomes: 7
Your program should then display the resulting output. A sample run of the program, with
the user input in bold, is shown below:
1 >>> Enter some text: I like to eat eggs and spam.
2
3 I 1ik3 70 347 3gg5 4nd 5p4m.
4
5 >>>

"""

"""
user_input = raw_input("Enter some text:")
print(user_input)


user_input[user_input.find("a")]

print(user_input)
"""


my_text = raw_input("Enter some text: ")

my_text = my_text.replace("a", "4")
my_text = my_text.replace("b", "8")
my_text = my_text.replace("e", "3")
my_text = my_text.replace("l", "1")
my_text = my_text.replace("o", "0")
my_text = my_text.replace("s", "5")
my_text = my_text.replace("t", "7")

print(my_text)