age = 14
height = 1.83

#time for math now (yay!)

# Area of a triangle
# area = 0.5 x b x h

# # ask user for base 
# base = int(input('BASE NOW '))
# # ask user for height
# height = int(input('HEIGHT NOW '))
# # calculate area
# area = base * height * 0.5

# # print area
# print(f'the area is:{area}')

# -----------
# Calculate perimeter for triangle
# p = a + b + c

# # ask user for side a
# sideA = int(input('SIDE A AT ONCE! '))
# # ask user for side b
# sideB = int(input('SIDE B IF YOU PLEASE '))
# # ask user for side c
# sideC = int(input('SIDE C NOW! '))
# # caclulate perimeter
# perimiter = sideA + sideB + sideC
# # print perimeter
# print(f'the perimiter is: {perimiter}')

# -----------
# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + w
# ask user for lenth
# length = int(input('what would be the length of the rectangle? '))
# # ask user for height
# height = int(input('what would be the height of the rectangle? '))
# # calculate area
# area = length * height
# # calculate perimeter
# perimiter = 2 * (length + height)
# # print both area and perimeter
# print(f'area: {area},perimiter: {perimiter}')

# ----------------
# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# # ask user for radius
# radius = int(input('what is the radius? '))
# # calculate area
# area = radius **2 * 3.14
# # calculate circumference
# circum = 2 * 3.14 * radius

# # print both
# print(f'the area is: {area} and the circumference is: {circum}')

#---------------
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len('python') != len('dragon'):
    print('they are not the same length')



#-----------
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print('on is in both words')


#----------
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon.':
    print('jargon is in the sentence')

print('jargon' in 'I hope this course is not full of jargon')


# ----------
# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))



# --------------------
# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
# number = 24
# number = int(input('please type number '))
# if number % 2 == 0:
#     print('number is even')
# else:
#     print('number is odd')


# ------------
# Check if type of '10' is equal to type of 10

print('10'== 10) 
print('10' is 10)


#---------
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours = float(input('hours worked: '))
# rate = float(input('how much u get payed per hour, hombre? '))
# pay = rate * hours
# print(f'your pay is: {pay}')


#--------
#Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
age = float(input('how old are you? '))
seconds = age * 365 * 24 * 60 * 60
print(seconds)