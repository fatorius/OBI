num_quadrados = int(input())
quadrados = input().split()

def dist_direita(quadrado):
    for i in range(num_quadrados):
        if quadrado+i == num_quadrados-1:
            return 99999
        if quadrados[quadrado+i+1] == "0":
            return i+1

def dist_esquerda(quadrado):
    for i in range(num_quadrados):
        if quadrado-i == -1:
            return 99999
        if quadrados[quadrado-i-1] == "0":
            return i+1

for i in range(num_quadrados):
    if quadrados[i] == "0":
        print(0, end=" ")
    else:
        print(min([dist_direita(i), dist_esquerda(i)]), end=" ")

print()