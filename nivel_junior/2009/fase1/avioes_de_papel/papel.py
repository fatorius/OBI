entrada = input().split()

competidores = int(entrada[0])
papel_comprado = int(entrada[1])
papel_recebido = int(entrada[2])

if competidores * papel_recebido <= papel_comprado:
    print("S")
else:
    print("N")
