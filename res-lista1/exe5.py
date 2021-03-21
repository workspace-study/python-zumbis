p = int(input('Preco do Produto: '))
d = float(input('Qual desconto%: '))

desconto = p * d / 100
valor = p - desconto

print(f'Com desconto de: {desconto}(%)')
print(f'O valor do produto fica: R$ {valor:.2f}')