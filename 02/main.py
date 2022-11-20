#Hoy es dia numero dos
first_name = 'LeBron'
last_name = 'James'
full_name = first_name + ' ' + last_name
country = 'America'
city = 'Akron'
age = 38
year = 1984
is_married = True
is_dead = False
team_location, team_name = 'Los Angeles', 'Lakers'

#level numero dos
print(type(first_name))
print(type(age))
print(type(is_married))
# print(len(first_name))
print(f'The first name is {len(first_name)} characters long')

if len(first_name) > len(last_name):
    print('the first name is longer')
elif len (first_name) == len(last_name):
    print('they are equally long')
else:
    print('the last name is longer')

#new very cool math section

num1 = 5
num2 = 4
total = num1 + num2
diff = num1 - num2
product = num1 * num2
division = num1 / num2
remainder = num2 % num1
exp = num1 ** num2
print(f'num1:{num1} num2:{num2} total:{total} diff:{diff} product:{product} division:{division} remainder:{remainder} exp:{exp}')

#circle
#pi x radius squared
radius = 30
pi = 3.14
area = pi * radius ** 2
print(f'radius:{radius} pi:{pi} area:{area}')

#2 x pi x radius
print(f'radius:{radius} pi:{pi} circum:{pi * 2 * radius}')


# Based on use input

# ask user to "enter radius" and assign input to variable radius making sure it's a number
radius = int(input('enter radius NOW '))
area = pi * radius ** 2
circum = pi * 2 * radius
print(f'the area is {area} and the circumferance is {circum}')
# calculate area

# calculate circum

# print area and circum