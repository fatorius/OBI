tempos = []

tempos.append(int(input()))
tempos.append(int(input()))
tempos.append(int(input()))

print(tempos.index(min(tempos)) + 1)
tempos[tempos.index(min(tempos))] = 1001 # Atribui um valor acima do limite para que esse competidor não seja medalhista novamente
print(tempos.index(min(tempos)) + 1)
tempos[tempos.index(min(tempos))] = 1001 # Atribui um valor acima do limite para que esse competidor não seja medalhista novamente
print(tempos.index(min(tempos)) + 1)
tempos[tempos.index(min(tempos))] = 1001 # Atribui um valor acima do limite para que esse competidor não seja medalhista novamente
