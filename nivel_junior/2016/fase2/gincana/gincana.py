# Esse código também ficou extremamente bagunçado mas só consegui pensar nessa solução
# Apesar de tantos loops aninhados, este código ainda é rápido ao executar

entrada = input().split()

rival = int(entrada[0])
turma = int(entrada[1])

delegacao = turma

def primo(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

encontrado = False

while delegacao != 0:
    k = delegacao

    while k <= turma:
        k -= 1
        if k == 1:
            print(1)
            encontrado = True
            break
        if not primo(k):
            continue
        if delegacao % k != 0 and rival % k != 0:
            print(k)
            encontrado = True
            break
    
    if encontrado:
        break

    delegacao -= 1
