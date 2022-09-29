x = 5               # int
y = 2.5             # float
name = 'Bob'        # str
isOnline = True     # bool

print(type(x))          # <class 'int'>
print(type(y))          # <class 'float'>
print(type(name))       # <class 'str'>
print(type(isOnline))   # <class 'bool'>


# type conversion
# int to float
x = float(x)
print(x)        # output: 5.0 > float
print(type(x))  # <class 'float'>

# float to int
y = int(y)
print(y)        # output: 2 > int
print(type(y))  # <class 'int'>

'''
# bool to int

isOnline = int(isOnline)
print(isOnline)         # output: 1 > int
print(type(isOnline))   # <class 'int'>
'''

result = x + y + isOnline
print(result)
print(type(result))
# output: 8.0

result = str(x) + str(y) + str(isOnline)
print(result)
print(type(result))
# output: 5.02True
