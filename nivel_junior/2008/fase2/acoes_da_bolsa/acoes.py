from numpy import var


dias = int(input())
variacao = input().split()

for i in range(dias):
    variacao[i] = int(variacao[i])

maior_lucro = variacao[0] + variacao[1] + variacao[2] + variacao[3]

for seq in range(1, dias - 3):
    lucro = variacao[seq] + variacao[seq+1] + variacao[seq+2] + variacao[seq+3]
    if lucro > maior_lucro:
        maior_lucro = lucro

print(maior_lucro)