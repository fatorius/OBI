tipos_de_balas = int(input())

rotulos = input().split()

for i in range(tipos_de_balas):
    rotulos[i] = int(rotulos[i])

print(min(rotulos))