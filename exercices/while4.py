n = 1
# acumulador pode ser de produto
soma = 0

while n <= 10:
    x = int(input(f'{n} numero: '))
    soma = soma + x
    n = n + 1
media = soma / 10
print(f'Media: {media}')