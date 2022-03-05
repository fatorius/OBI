# Esse código ficou meio bagunçado então tive que recorrer aos comentarios
# para tentar torná-lo compreensível

''' 
Aqui recebemos os valores de entrada
e separamos cada um deles em variáveis 
mais específicas convertendo-os para int
(uma vez que todos os valores serão inputados em uma linhas só)
'''
numeros = input().split()

numerador1 = int(numeros[0])
denominador1 = int(numeros[1])
numerador2 = int(numeros[2])
denominador2 = int(numeros[3])

'''
Aqui estão duas funções que serão usadas ao longo
do programa, coloquei-as como funções para que o 
código fique menos bagunçado
'''
def MMC(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return (num1 * num2) / a

def MDC(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a

# O primeiro passo para fazer a soma de duas frações é tirar o MMC dos denominadores
mmc = MMC(denominador1, denominador2) # A partir de agora o MMC agirá como denominador da fração final

'''
Depois de obter o MMC devemos dividi-lo pelo
denominador e multiplicá-lo pelo numerador
de cada um dos termos da soma
O resultado será o novo numerador de cada fração

Dessa forma temos duas "frações equivalentes" às
da soma original, a diferença é que essas têm o mesmo
denominador (o denominador comum que no caso é o MMC)

Em outras palavras, agora estamos somando 
(numerador1) / MMC + (numerador2) / MMC
'''
numerador1 = (mmc // denominador1) * numerador1
numerador2 = (mmc // denominador2) * numerador2

'''
Uma vez que ambos os denominadores estão iguais, 
podemos simplesmente somar os numeradores e manter o 
denominador.

O resultado vou chamar de fração final
'''
numerador = numerador1 + numerador2

# Calculamos o MDC para obter a forma irredutível da fração final
mdc = MDC(numerador, mmc)

'''
O último passo é dividir o numerador e o denominador (MMC) 
da fração final pelo MDC. Fiz isso na mesma linha que imprime
os números na tela.

É importante notar que o resultado foi convertido para INT.
Isso foi necessário porque em Python todo resultado de divisão
se torna FLOAT, sendo assim, mesmo que a divisão desse um resultado
inteiro, ele ainda seria exibido com ".0" no final, o que pode 
causar conflito na correção da OBI
'''
print("{} {}".format(int(numerador / mdc), int(mmc / mdc)))

# Complicadinho esse....