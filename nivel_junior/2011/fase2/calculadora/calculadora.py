operacoes = int(input())

resultado = 1

for i in range(operacoes):
    conta = input().split()

    if conta[1] == "/":
        resultado /= int(conta[0])
    else:
        resultado *= int(conta[0])

print(int(resultado))