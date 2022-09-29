x = input('enter number-x: ')
y = input('enter number-y: ')

sum = x + y

print(sum)

# input() function is used to take user input. By default, it returns the user input in form of a string.
'''
enter number1: 10
enter number2: 20
1020

'''

a = input('enter number-a: ')
b = input('enter number-b: ')

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