bandejas = int(input())

copos_derrubados = 0

for i in range(bandejas):
    bandeja = input().split()

    latas = int(bandeja[0])
    copos = int(bandeja[1])

    if latas > copos:
        copos_derrubados += copos

print(copos_derrubados)