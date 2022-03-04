entrada = input().split()
postos = input().split()

quant_postos = int(entrada[0])
distancia = int(entrada[1])

for n, metros in enumerate(postos):
    metros = int(metros)
    if n == quant_postos-1:
        if 42195 - metros > distancia:
            print("N")
        else:
            print("S")
        break
    if int(postos[n+1]) - metros > distancia:
        print("N")
        break

