coordenadas = input().split()

x = int(coordenadas[0])
y = int(coordenadas[1])

if x < 0 or y < 0 or x > 432 or y > 468:
    print("fora")
else:
    print("dentro")