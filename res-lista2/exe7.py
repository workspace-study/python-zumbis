m = int(input('Metragem: '))

if m % 54 == 0:
    latas = m / 54
else:
    latas = int(m / 54) + 1

valor = latas * 80

print(f'{latas} latas')
print(f'TOtal: R$ {valor:.2f}')