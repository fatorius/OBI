lia = sorted([int(input()), int(input())])
carolina = sorted([int(input()), int(input())])

pontos_lia = sum(lia)
pontos_carolina = sum(carolina)

if lia[0] == lia[1]:
    pontos_lia *= 2
elif lia[0] == lia[1] - 1:
    pontos_lia *= 3

if carolina[0] == carolina[1]:
    pontos_carolina *= 2
elif carolina[0] == carolina[1] -1:
    pontos_carolina *= 3

if pontos_lia == pontos_carolina:
    print("empate")
elif pontos_lia > pontos_carolina:
    print("Lia")
else:
    print("Carolina")