tabuleiro = []

for i in range(15):
    tabuleiro.append(input().split())

for i in range(15):
    for j in range(15):
        if tabuleiro[i][j] == "0":
            continue
        else: 
            pedra = tabuleiro[i][j]
            
            # Checagem de 5 pedras na linha:
            if j <= 10:
                for l in range(1, 5):
                    if tabuleiro[i][j+l] != pedra:
                        break
                    if l == 4:
                        print(pedra)
                        exit()
            
            # Checagem de 5 pedras na coluna
            if i <= 10:
                for c in range(1, 5):
                    if tabuleiro[i+c][j] != pedra:
                        break
                    if c == 4:
                        print(pedra)
                        exit()

            # Checagem de 5 pedras na diagonal
            if i <= 10 and j <= 10:
                for d in range(1, 5):
                    if tabuleiro[i+d][j+d] != pedra:
                        break
                    if d == 4:
                        print(pedra)
                        exit()

print(0)