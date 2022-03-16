'''
Esse é outro exercício que eu lembro de ter resolvido 
lá em 2018 (se eu não me engano ele também fez parte da prova
de nível 1) e O PROGRAMA QUE EU FIZ ERA TÃO RUIM ASKDASDKASKDASDKAS
Tanto é que ele não passou nos testes e eu não consegui passar 
para a terceira fase...
'''

lu = int(input()) - 1
kung = int(input()) - 1

etapas = ["oitavas", "quartas", "semifinal", "final"]

for i in range(4):
    lu = lu // 2
    kung = kung // 2

    if lu == kung:
        print(etapas[i])
        break
