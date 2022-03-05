from numpy import sort


aposta = input().split()
sorteados = input().split()

acertos = 0

for num in aposta:
    if num in sorteados:
        acertos += 1

if acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
elif acertos == 6:
    print("sena")
else:
    print("azar")