dims = int(input())

tabuleiro = []

for i in range(dims):
    tabuleiro.append(input().split())

for i in range(dims):
    for j in range(dims):
        if tabuleiro[i][j] != "9":
            continue
        vizinhos = [tabuleiro[i-1][j-1],
                    tabuleiro[i][j-1],
                    tabuleiro[i-1][j]]
        tabuleiro[i][j]= min(set(vizinhos), key=vizinhos.count)

print(tabuleiro[dims-1][dims-1])