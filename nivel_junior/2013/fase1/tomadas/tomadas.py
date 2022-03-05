reguas = input().split()

total = 0

for regua in reguas:
    total += int(regua) - 1

print(total+1)

# Talvez não seja a maneira mais inteligente de resolver esse problema mas 
# o importante é que funciona...
