tamanho = int(input())
montanha = input().split()

picos = 0

for i in range(tamanho):
    montanha[i] = int(montanha[i])

for i in range(1, tamanho-1):
    if montanha[i-1] < montanha[i] and montanha[i] > montanha[i+1]:
        picos += 1

if picos > 1:
    print("S")
else:
    print("N")