p = int(input()) # 1 se Bob = Par

bob = int(input())
alice = int(input())

soma = bob + alice

par = soma % 2

if par == p:
    print("0")
else:
    print("1")
