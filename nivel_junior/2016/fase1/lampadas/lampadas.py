a = False
b = False

i1 = False 
i2 = False

apertos = int(input())
interruptores = input().split()

for interruptor in interruptores:
    if interruptor == "1":
        i1 = not i1
        a = not a
    else:
        i2 = not i2
        a = not a
        b = not b

if a:
    print(1)
else:
    print(0)
if b:
    print(1)
else:
    print(0)