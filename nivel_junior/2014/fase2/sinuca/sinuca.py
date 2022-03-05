bolas = int(input())

fileira_anterior = input().split()

while bolas != 1:
    fileira_atual = []
    for bola in range(bolas-1):
        if fileira_anterior[bola] == fileira_anterior[bola+1]:
            fileira_atual.append("1")
        else:
            fileira_atual.append("-1")
    bolas -= 1
    fileira_anterior = fileira_atual

if fileira_anterior[0] == "1":
    print("preta")
else:
    print("branca")