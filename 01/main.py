import math


print (2+2)
print (2-1)
print (2*2)
print(4/2)
print(2**4)
print(5%6)

#i will check types

print (type(7))
print(type(2.3))
print(type('penis'))

penis = 'penis_2'

print(type(penis))

cock = {
    'team1' : 'bucks',
    'team2' : 'hornets',
    'winner' : 'bucks',
}

print(type(cock))
print(cock['winner'])
print(cock['winner'])

cock2 = {
    '1' : 'charlotte hornets = bad',
    '2' : 'milwaukee bucks = good',
    '3' : 'memphis grizzlies = mid',
    '4' : 'Giannis = god',
}
print(cock2['1'])
print(cock2['2'])
print(cock2['3'])
print(cock2['4'])


cock3 = [
     'charlotte hornets = bad',
     'milwaukee bucks = good',
     'memphis grizzlies = mid',
     'Giannis = god',
]

# print(cock3[])
# print(cock3[])

grades = ['pass', 'superb', 'fail']


# Eucledian distance

p = (2,3)
q = (10,8)

# distance = square root of (q1 - p1)^2 + (q2 - p2)^2
# p => (p1, p2)
# q => (q1, q2)

ones = (q[0] - p[0]) ** 2
twos = (q[1] - p[1]) ** 2
sum = ones + twos
distance = math.sqrt(sum)
print(distance)