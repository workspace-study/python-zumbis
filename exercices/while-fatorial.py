k = 1
# acumulador neutro de fatorial é 1
fat = 1
n = int(input('n: '))

while k <= n:
    fat = fat * k
    k = k + 1
print(f'fat(n) = {fat}')