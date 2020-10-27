# 1
"""
a, b, c = eval(input('a,b,c='))
if a > b:
    maX = a
    miN = b
else:
    maX = b
    miN = a
if miN < c <maX:
    miD = c
if c > maX:
    miD = maX
    maX = c
elif c < miN:
    miD = miN
    miN = c
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 2
"""
a, b, c = eval(input('a,b,c='))
maX = max(a, b, c)
miN = min(a, b, c)
miD = (a + b + c) - (maX + miN)
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 3
"""
a, b, c = eval(input('a,b,c='))
maX = max(a, b, c)
miN = min(a, b, c)
if maX != a != miN:
    miD = a
elif maX != b != miN:
    miD = b
else:
    miD = c
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 4
"""
a, b, c = eval(input('a,b,c='))
maX, miN = (a, b) if a > b else (b, a)
if c < miN:
    miD = miN
    miN = c
elif c > maX:
    miD = maX
    maX = c
else:
    miD = c
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 5
"""
a, b, c = eval(input('a,b,c='))
maX, miN = (a, b) if a > b else (b, a)
maX, miD, miN = (c, maX, miN) if c > maX else ((maX, miN, c) if c < miN else (maX, c.miN))
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 6
"""
a, b, c = eval(input('a,b,c='))
maX, miD, miN = ((a, b, c) if b > c else ((a, c, b) if a > c else \
(c, a, b))) if a > b else ((c, b, a) if b < c else ((b, a, c) if a > c else (b, c, a)))
print('max={},mid={},min={}'.format(maX, miD, miN))
"""
# 11
"""
x = eval(input('x='))
if (x % 2) != 0:
    print('{}是奇数'.format(x))
else:
    print('{}是偶数'.format(x))
"""
# 12
"""
x = eval(input('x='))
if (x % 3 == 0) and (x % 5 != 0):
    print('AAA')
else:
    print('BBB')
"""
# 13
"""
x, y = eval(input('x,y='))
if (x ** 2 + y ** 2 > 1) and (x ** 2 + y ** 2 < 4):
    print('AAA')
else:
    print('BBB')
"""
# 15
a, b, c = eval(input('the length of the three sides is: '))
if a + b > c and a + c > b and abs(b + c) > a and abs(a - b) < c  and abs(a - c) < b and abs(b - c) < a:
    print("the three numbers are able to be a triangle!")
    if a == b ==c:
        print("And it is an Equilateral triangle!")
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print("And it is an isosceles triangle")
    elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (c ** 2 + b ** 2 == a ** 2):
        print("And it is a right triangle!")
else:
    print("the three numbers are NOT able to be a triangle")
