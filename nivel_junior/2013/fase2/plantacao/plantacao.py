entrada = input().split()

total_dias = int(entrada[0])
total_arvores = int(entrada[1])

total = 0
arvores = []

frutas = input().split()
chuvas = input().split()

for fruta in frutas:
    arvores.append(int(fruta))
    
for dia in range(total_dias):
    if chuvas[dia] == "C":
        for i, arvore in enumerate(arvores):
            if arvore == 0:  # ignorar arvores mortas
                continue
            total += arvore + 1
            arvores[i] = arvore + 1
    else:
        for i, arvore in enumerate(arvores):
            if arvore == 0:  # ignorar arvores mortas
                continue
            total += arvore - 1
            arvores[i] = arvore - 1
            
print(total)