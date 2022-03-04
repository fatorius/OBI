consultas = int(input())

consultas_realizadas = 0

consulta_inicio = 0
consulta_fim = 0

for i in range(consultas):
    horarios = input().split()

    inicio = int(horarios[0])
    fim = int(horarios[1])

    if inicio >= consulta_fim:
        consultas_realizadas += 1
        consulta_inicio = inicio
        consulta_fim = fim

print(consultas_realizadas)   
