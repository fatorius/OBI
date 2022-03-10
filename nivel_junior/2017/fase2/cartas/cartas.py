cartas = [int(input()), int(input()), int(input())]

print(min(set(cartas), key=cartas.count))
