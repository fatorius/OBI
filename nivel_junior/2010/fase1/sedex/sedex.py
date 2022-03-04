diametro = int(input())
dimensoes = input().split()

cabe = True

for dimensao in dimensoes:
    if diametro > int(dimensao):
        cabe = False
        break

if cabe:
    print("S")
else:
    print("N")