# Jesus amado...

from isort import file


def coord(x, y):
    x -= 1
    y -= 1

    return (x * fileiras) + y

def passa_bolinha(x, y):
    aluno = coord(x, y)
    
    bandeiras[aluno] = True
    numero_atual = alunos[aluno]

    # colega 1 = y + 1
    if y != fileiras:
        colega = coord(x, y+1)
        if alunos[colega] >= numero_atual and not bandeiras[colega]:
            passa_bolinha(x, y+1)
    
    # colega 2 = x + 1
    if x != fileiras:
        colega = coord(x+1, y)
        if alunos[colega] >= numero_atual and not bandeiras[colega]:
            passa_bolinha(x+1, y) 
    # colega 3 = y - 1

    if y != 1:
        colega = coord(x, y-1)
        if alunos[colega] >= numero_atual and not bandeiras[colega]:
            passa_bolinha(x, y-1)

    # colega 4 = x - 1  
    if x != 1:
        colega = coord(x-1, y)
        if alunos[colega] >= numero_atual and not bandeiras[colega]:
            passa_bolinha(x-1, y)
            
fileiras = int(input())

coord_inicial = input().split()

alunos = []
bandeiras = []

for fileira in range(fileiras):
    numeros = input().split()
    for numero in numeros:
        alunos.append(int(numero))
        bandeiras.append(False)

passa_bolinha(int(coord_inicial[0]), int(coord_inicial[1]))

print(bandeiras.count(True))