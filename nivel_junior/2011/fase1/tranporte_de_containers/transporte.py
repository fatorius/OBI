container = input().split()
navio = input().split()

# Quantidade de containers em cada uma das dimensões
largura = int(navio[0]) // int(container[0])
altura = int(navio[1]) // int(container[1])
profundidade = int (navio[2]) // int(container[2])

print(largura * altura * profundidade)