entrada = input().split()

pontos_c = (int(entrada[0]) * 3) + (int(entrada[1]) * 1)
pontos_f = (int(entrada[3]) * 3) + (int(entrada[4]) * 1)

if pontos_c > pontos_f:
    print("C")
elif pontos_c < pontos_f:
    print("F")
else:
    saldo_c = int(entrada[2])
    saldo_f = int(entrada[5])
    
    if saldo_c < saldo_f:
        print("F")
    elif saldo_c > saldo_f:
        print("C")
    else:
        print("=")
