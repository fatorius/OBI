entrada = input().split()

competidores = int(entrada[0])
voltas = int(entrada[1])

competidor_atual = 0
vencedor = 0
melhor_tempo = 99999

for i in range(competidores):
    competidor_atual += 1

    tempo_atual = 0

    tempos = input().split()

    for tempo in tempos:
        tempo_atual += int(tempo)
    
    if tempo_atual < melhor_tempo:
        melhor_tempo = tempo_atual
        vencedor = competidor_atual

print(vencedor)