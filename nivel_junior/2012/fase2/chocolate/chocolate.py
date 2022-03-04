centimetros = int(input())

barras = 1

while centimetros >= 2:
    barras *= 4
    centimetros /= 2

print(barras)