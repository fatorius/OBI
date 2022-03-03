texto = input()

def traduz(letra):
    if letra == "A" or letra == "B" or letra == "C":
        return 2
    elif letra == "D" or letra == "E" or letra == "F":
        return 3
    elif letra == "G" or letra == "H" or letra == "I":
        return 4
    elif letra == "J" or letra == "K" or letra == "L":
        return 5
    elif letra == "M" or letra == "N" or letra == "O":
        return 6
    elif letra == "P" or letra == "Q" or letra == "R" or letra == "S":
        return 7
    elif letra == "T" or letra == "U" or letra == "V":
        return 8
    elif letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
        return 9
    else:
        return "-"

for letra in texto:
    print(traduz(letra), end="")
print()