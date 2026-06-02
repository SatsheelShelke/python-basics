print('Calculator')
n1 = float(input('Num 1= '))
n2 = float(input('Num 2= '))
print('')
print('Choose operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = int(input('Selected option: '))

if choice == 1:
    print('Answer =', n1 + n2)
elif choice == 2:
    print('Answer =', n1 - n2)
elif choice == 3:
    print('Answer =', n1 * n2)
elif choice == 4:
    if n2 == 0:
        print('Cannot divide by zero''Answer =', n1 / n2)
    else:
        print('Answer =', n1 / n2)
else:
    print('Invalid choice')
