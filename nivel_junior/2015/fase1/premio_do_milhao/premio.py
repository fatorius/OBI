dias = int(input())

acessos = 0
dias_necessarios = 0

for dia in range(dias):
    if acessos < 1000000:
        dias_necessarios += 1
    acessos += int(input())

print(dias_necessarios)