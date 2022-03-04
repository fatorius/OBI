celula = int(input())

campo = []

for i in range(celula):
    campo.append(input())

celula -= 1

for i in range(celula + 1):
    bombas = 0

    if campo[i] == "1":
        bombas += 1

    if i < celula:
        if campo[i+1] == "1":
            bombas += 1
    if i > 0:
        if campo[i-1] == "1":
            bombas += 1

    print(bombas)