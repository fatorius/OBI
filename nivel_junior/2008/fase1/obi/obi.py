competidores, pontos = input().split()

convidados = 0
pontos = int(pontos)

for i in range(int(competidores)):
    x, y = input().split() #X = Nota da primeira fase, Y = Nota da segunda fase 
    if int(x) + int(y) >= pontos:
        convidados += 1

print(convidados)
