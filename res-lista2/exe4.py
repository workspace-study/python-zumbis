a = int(input('Num1: '))
b = int(input('Num2: '))
c = int(input('Num3: '))

if a >= b and a >= c:
    print(f'Maior: {a}')
elif b>= c:
    print(f'Maior: {b}')
else:
    print(f'Maior: {c}')