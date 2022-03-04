pessoas = int(input())

segundos = 0

proxima_parada = 0

for pessoa in range(pessoas):
    tempo = int(input())

    if tempo >= proxima_parada:
        segundos += 10
        proxima_parada = tempo + 10
    else:
        segundos += 10 - (proxima_parada - tempo)
        proxima_parada += 10 - (proxima_parada - tempo)

print(segundos)
