min = int(input('Minutos: '))

# ERRADO
#if min < 200:
#    conta = min * 0.20
#    print('Sua conta é de: ', conta)
#if min > 200 or min < 400:
#    conta = min * 0.18
#    print('Sua conta é de: ', conta)
#if min > 400:
#    conta = min * 0.15
#    print('Sua conta é de: ', conta)

# CORRETO
if min < 200:
    preco = 0.2
else:
    if min <=400:
        preco = 0.18
    else:
        preco = 0.15
print(f'R$ {preco*min:.2f}')