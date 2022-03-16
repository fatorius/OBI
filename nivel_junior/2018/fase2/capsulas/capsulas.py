'''
Essa aqui na época eu até desisti de fazer
de tão complicada que eu achava que era...
'''

linha1 = input().split()

capsulas = int(linha1[0])
meta = int(linha1[1])

ciclos = input().split()

for i in range(capsulas):
    ciclos[i] = int(ciclos[i])

dias = 0
total = 0

while total < meta:
    dias += 1

    for ciclo in ciclos:
        if dias % ciclo == 0:
            total += 1

print(dias)