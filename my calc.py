# take input for operator and operand
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
operator = input('Enter the operator: ')

# lets print the type of the variables
print(type(number1), type(number2))

# converting the type of variables
number1 = int(number1)
number2 = int(number2)

# lets print the type of the variables
print(type(number1), type(number2))

# let's check the operator first
result = ''
if operator == '+':
  result = number1 + number2
elif operator == '-':
  result = number1 - number2
elif operator == '*':
  result = number1 * number2
elif operator == '/':
  result = number1 / number2
else:
  result = 'Not defined'

# lets print it
print('The result is : ', result)
