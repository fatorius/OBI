dimensao1, dimensao2, dimensao3 = int(input()), int(input()), int(input()) # Lembrei que dá pra fazer isso kkkk

area = int(input()) * int(input())

if dimensao1 * dimensao2 <= area or dimensao1 * dimensao3 <= area or dimensao2 * dimensao3 <= area:
    print("S")
else:
    print("N")

"""
Uma outra forma de resolver 
consiste em verificar se existe pelo menos uma dimensão da
caixa menor que a altura da janela, e outra dimensão 
(que não seja a primeira) menor que a largura da janela
O único problema com essa solução é que o código seria muito bagunçado 
e desnecessariamente dificil de entender
"""