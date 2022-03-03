'''
COMENTARIO SOBRE ESTA SOLUÇÃO 

Creio que haja um erro no texto da questão,
onde eles informam que o primeiro inteiro da entrada (N)
corresponde à quantidade de bits que a calculadora processa.

Mais acima no texto eles informam que a calculadora não consegue
processar números iguais ou maiores que 2 elevado a quantidade de bits.

Sendo assim, a primeira impressão é de que teremos que elevar 
2 à quantidade de bits e fazer com que a simplificação
deixe tanto o dividendo quando o divisor menores que esse valor.

Porém ao observar os exemplos dados na questão, vemos que isso não faz sentido,
pois em todos os casos a calculadora seria capaz de realizar a divisão 
sem precisar de nenhuma simplificação.

Isso me levou a crer que o primeiro inteiro da entrada (N) na verdade
corresponde ao VALOR LIMITE que a calculadora suporta, portanto
a simplificação deve manter tanto o dividendo quanto o divisor abaixo 
desse valor. (O que explica porque o segundo exemplo dá IMPOSSIVEL como resultado
enquanto o terceiro não)

Tentei confirmar essa hipótese submentendo o código para correção no site 
https://olimpiada.ic.unicamp.br/pratique/pj/2008/f2/minicalc/corrige/
porém essa página sempre me retorna erro

Caso ache que minha solução esteja errada, por favor entre em contato pelo email
mail@hugosouza.com ou escreva um Issue report no repositório do GitHub
https://github.com/fatorius/OBI

HugoSouza 03/03/2022
'''

entrada = input().split()

bits = int(entrada[0])
dividendo = int(entrada[1])
divisor = int(entrada[2])

def MDC(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a

mdc = MDC(dividendo, divisor)

dividendo /= mdc
divisor /= mdc

if dividendo > bits or divisor > bits:
    print("IMPOSSIVEL")
else:
    print("{} {}".format(int(dividendo), int(divisor)))