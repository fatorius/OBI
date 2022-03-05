entrada = input().split()

volume = int(entrada[0])
trocas = input().split()

for troca in trocas:
    troca = int(troca)

    # Essa logica de min e max evita que o volume da TV 
    # ultrapasse os limites do volume máximo e volume mínimo
    if troca > 0:
        volume = min([100, volume + troca])
    else:
        volume = max([0, volume + troca])

print(volume)