entrada = input().split()

paises = int(entrada[0])
modalidades = int(entrada[1])

medalhas = [0] * paises

for i in range(modalidades):
    medalhistas = input().split()
    for medalhista in medalhistas:
        medalhas[int(medalhista) - 1] += 1

vencedores = list(sorted(zip(medalhas, range(1, paises+1)), reverse=True))

final = []

for i, pais in enumerate(vencedores):
    if  i != len(vencedores) - 1:
        if pais[0] == vencedores[i+1][0]:
            if pais[1] > vencedores[i+1][1]:
                vencedores[i], vencedores[i+1] = vencedores[i+1], vencedores[i]

for vencedor in vencedores:
    print(vencedor[1], end=" ")

print()