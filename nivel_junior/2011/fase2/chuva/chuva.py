dimensao = int(input())

mapa1 = []
mapa2 = []

for i in range(dimensao):
    dados = input().split()
    mapa = []
    for dado in dados:
        mapa.append(int(dado))
    mapa1.append(mapa)

for i in range(dimensao):
    dados = input().split()
    mapa = []
    for dado in dados:
        mapa.append(int(dado))
    mapa2.append(mapa)
        
for linha in range(dimensao):
    for coluna in range(dimensao):
        print(mapa1[linha][coluna] + mapa2[linha][coluna], end=" ")
    print()
