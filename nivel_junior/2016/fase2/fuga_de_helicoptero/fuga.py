"""
ATENÇÃO

ESTA NÃO É A SOLUÇÃO MAIS EFICIENTE PARA ESTE PROBLEMA
O LOOP WHILE CONSOME UM TEMPO QUE NÃO PRECISARIA SER GASTO

EU ESCREVI ESTA SOLUÇÃO DESSA MANEIRA POIS ACHEI MAIS FACIL DE COMPREENDER O CÓDIGO
DESSA FORMA
"""

valores = input().split()

helicoptero = int(valores[0])
policial = int(valores[1])
fugitivo = int(valores[2])
direcao = int(valores[3])

pista = ["-"] * 16

pista[helicoptero] = "H"
pista[policial] = "P"

while True:
    fugitivo += direcao
    
    if fugitivo > 15:
        fugitivo = 0
    if fugitivo < 0:
        fugitivo = 15

    if pista[fugitivo] == "P":
        print("N")
        break
    elif pista[fugitivo] == "H":
        print("S")
        break
    else:
        continue