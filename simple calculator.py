def calculate():
  
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

     
    operations = ['+', '-', '*', '/']

 
    operation = input('''
+ for addition
- for subtraction
* for multiplication
/ for division
''')

   
    if operation == '+':
        print('{} + {} = '.format(a, b))
        print(a + b)

    elif operation == '-':
        print('{} - {} = '.format(a, b))
        print(a - b)

    elif operation == '*':
        print('{} * {} = '.format(a, b))
        print(a * b)

    elif operation == '/':
        print('{} / {} = '.format(a, b))
        print(a / b)

    else:
        print('You have not typed a valid operator, please run the program again.')

 
def again():

    
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

     
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
 
calculate()
again()