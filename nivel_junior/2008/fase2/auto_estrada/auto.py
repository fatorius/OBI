comprimento = int(input())
blocos = input()

paineis = 0

for bloco in blocos:
    if bloco == "P":
        paineis += 2
    elif bloco == "C":
        paineis += 2
    elif bloco == "A":
        paineis += 1

print(paineis)