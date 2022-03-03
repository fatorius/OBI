questoes = int(input())

gabarito_oficial = input()
gabarito_candidato = input()

acertos = 0

for i in range(questoes):
    if gabarito_oficial[i] == gabarito_candidato[i]:
        acertos += 1

print(acertos)