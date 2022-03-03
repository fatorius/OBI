entrada = input().split()

musicos = int(entrada[0])
pares = int(entrada[1])

entrosamentos = [0] * (musicos)

for par in range(pares):
    entrada = input().split()
    entrosamento = int(entrada[2])

    entrosamentos[int(entrada[0]) - 1] += entrosamento
    entrosamentos[int(entrada[1]) - 1] += entrosamento
    
banda = list(sorted(zip(entrosamentos, range(pares)), reverse=True)[:3])
banda = sorted([banda[0][1] + 1, banda[1][1] + 1, banda[2][1] + 1])
print("{} {} {}".format(banda[0], banda[1], banda[2]))
