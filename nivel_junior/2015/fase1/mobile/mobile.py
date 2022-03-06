a = int(input())
b = int(input())
c = int(input())
d = int(input())

equilibrado = (a == b + c + d) and (b + c == d) and (b == c)

if equilibrado:
    print("S")
else:
    print("N")