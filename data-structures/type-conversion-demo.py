'''
area of circle: πr^2
circumference of the circle: 2πr

calculate the area and circumference of the circle
π: 3.14
'''

'''
r = 3.14
π = 3.14

area = π * r * r
print(area)
# 30.959144000000002

circumference = 2 * π * r
print(circumference)
# 19.7192
'''

pi = 3.14

r = float(input('r of the circle: '))      # user input

area = pi * (r ** 2)
circumference = 2 * pi * r

print(type(area))
print(type(circumference))

'''
print('area: ', area)
print('circumference: ', circumference)
'''
print('area: '+ str(area) + ' circumference: '+ str(circumference))     # combining strings in one line and convert float to string

