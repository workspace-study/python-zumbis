km = float(input('Km Rodados: '))
dias = int(input('Dias: '))
preco = 60 * dias + 0.15 * km
print(f'R$ {preco:.2f}')