limite = int(input())

calculo = input().split()

operacao = calculo[1]

if operacao == "+":
    if int(calculo[0]) + int(calculo[2]) > limite:
        print("OVERFLOW")
    else:
        print("OK")
else:
    if int(calculo[0]) * int(calculo[2]) > limite:
        print("OVERFLOW")
    else:
        print("OK")