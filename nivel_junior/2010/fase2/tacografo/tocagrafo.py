intervalos = int(input())

distancia = 0

for i in range(intervalos):
    medida = input().split()

    distancia += int(medida[0]) * int(medida[1])

print(distancia)