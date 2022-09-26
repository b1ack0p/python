# Net salary calculation

print(7000 - (7000 * 0.15))     # Net salary of Alex: 5950.0
print(6500 - (6500 * 0.15))     # Net salary of Max: 5525.0

# lets define variables for this calculation:

salaryAlex = 7000
salaryMax = 6500
tax = 0.15

print(salaryAlex - (salaryAlex * tax))  # Net salary of Alex: 5950.0
print(salaryMax - (salaryMax * tax))    # Net salary of Max: 5525.0

#---------------------------------------------

number1 = 10
print(number1)      # if there is only one variable for number1 it will print the value >> 10

number1 = 20
print(number1)      # if there is a new variable for number1 it will print the last value >> 20

number1 += 30
print(number1)      # if you add another variable for number1 it will print the sum of 1st and 2nd values >> 50


# case sensitivity

age = 25
AGE = 37
Age = 51
agE = 48

print(age)
print(AGE)
print(Age)
print(agE)


# strings - int - float - bool

x = 2               # int
y = 3.4             # float
name1 = "John"      # string
name2 = 'Bob'       # string
isStudent = True    # bool True/False

# can be written in a single line as > x, y, name1, name2, isStudent = (2, 3.4, John, Bob, True)

#----------------------------------------------

a = 10
b = 20
x = '10'
y = '20'

print(a + b)        # 30
print('a' + 'b')    # ab
print(x + y)        # 1020

#----------------------------------------------

firstName = 'James'
lastName = ' Bond'

print(firstName + lastName)     # James Bond

