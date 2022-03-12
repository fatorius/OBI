total = int(input())
compradas = int(input())

figurinhas = []

for i in range(compradas):
    figurinhas.append(input())

print(total - len(set(figurinhas)))