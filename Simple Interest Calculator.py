print('SIMPLE INTEREST CALCULATOR')
p=float(input('principal:'))
r=float(input('rate:'))
t=float(input('time:'))
si=p*r*t/100
print('Simple Interest =', si)
print('Total Amount =', p + si)
