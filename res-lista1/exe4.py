atual_salario = float(input('Salario: '))
aumento = float(input('Aumento(%): '))

aumenta = atual_salario * aumento / 100
novo_salario = atual_salario + aumenta

print(f'Aumento: R$ {aumenta:.2f}')
print(f'Novo salario: R$ {novo_salario:.2f}')