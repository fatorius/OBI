ingredientes = input().split()

farinha = int(ingredientes[0])
ovos = int(ingredientes[1])
leite = int(ingredientes[2])

bolos = 0

while farinha >= 2 and ovos >= 3 and leite >= 5:
    bolos += 1
    farinha -= 2
    ovos -= 3
    leite -= 5

print(bolos)