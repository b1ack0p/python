x = input('enter number1: ')
y = input('enter number2: ')

sum = x + y

print(sum)

# input() function is used to take user input. By default, it returns the user input in form of a string.
'''
enter number1: 10
enter number2: 20
1020

'''


a = input('enter number1: ')
b = input('enter number2: ')

print(type(a))      # print type of 'a'
print(type(b))      # print type of 'b'

total = int(a) + int(b)     # convert strings to integer

print(total)

# output will be integer
'''
enter number1: 10
enter number2: 20
<class 'str'>
<class 'str'>
30
>> type of 'a' and 'b' values are 'string' but in 'total' variable with 'int(a)' and 'int(b)' function they are converted to 'integer'
'''