entrada = input().split()

numeros = []

for valor in entrada:
    numeros.append(int(valor))

print(max(numeros))