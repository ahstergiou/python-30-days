# # print('1\n2\n3\n')
# # print('1\t2\t3\t')


# ###
# # t e s t
# # 0 1 2 3
# # last index = 3

# # e   g   g
# # 0   1   2 (from the left)
# # -3  -2  -1 (from the right)
# # last index  = 2 

# # len(test) = 4
# # len(egg) = 3

# # last_index = len(string)

# name = 'alexander dallas stergiou'
# # print last letter of the sting contained in variable name
# last_letter = name[-1] 
# print(last_letter)

# last_index = len(name) - 1
# print(name[last_index], last_index)

# # check for palindrome
# word = 'level'

# # we want to check if the word == reversed word

# #print OK if the word is a palindrome
# if word[::-1] == word:
#     print('OK')
# else:
#     print('nah')

    

# function
# name(args)
# add(1,2)
# print('a',1)
# len()
# type ()
# input()

# methods
# string.something()
# string.capitalize() <=> capitalize(string)

# string methods

# word = 'alexander is cool'
# # capitalize
# # print(word.capitalize())
# # print('5'.capitalize())

# # count
# print(word.count('a'))

# # endswith
# print(word.endswith('l'))

# # find
# print(word.find('a'))

# # rfind
# print(word.rfind('l'))

# Exercises
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# print(type(sentence))
sentence = ['Thirty', 'Days', 'Of', 'Python']
to_print = ' '.join(sentence)
print(to_print)


# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'coding for all'

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the ch(aracters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.swapcase())

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('coding','python'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.


