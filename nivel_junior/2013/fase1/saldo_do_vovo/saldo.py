entrada = input().split()

transacoes = int(entrada[0])
saldo = int(entrada[1])

menor_saldo = saldo

for i in range(transacoes):
    transacao = int(input())

    saldo += transacao

    if saldo < menor_saldo:
        menor_saldo = saldo

print(menor_saldo)
