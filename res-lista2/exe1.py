a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triangulo')
    print('Um dos lados é maior que a soma dos dois lados')
elif a == b == c:
    print('Equilatero')
elif a == b or b == c or a == c:
    print('Isosceles')
