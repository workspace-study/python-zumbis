v = int(input('Velocidade KM: '))
# podemos apagar a linha abaixo e adicionar dentro do if
multa = 5

if v > 110:
    # multa = (v - 110) * 5
    valor = multa * (v - 110)
    print(f'Acima da velocidade. A multa é de: R$ {valor:.2f}')
else:
    print('Velocidade normal')