salario_h   = int(input('Ganho por hora: '))
h_mes       = int(input('Horas por mês: '))

bruto = salario_h * h_mes

ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05

liquido = bruto - ir -inss - sind

print(f'Salario bruto:\t\t R$ {bruto:.2f}')
print(f'IR:\t\t\t R$ {ir:.2f}')
print(f'INSS:\t\t\t R$ {sind:.2f}')
print(f'Salario liquido:\t R$ {liquido:.2f}')