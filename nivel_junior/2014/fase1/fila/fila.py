pessoas = int(input())
ids = input().split()
deixaram = int(input())
ids_deixaram = input().split()

for id in ids:
    if id not in ids_deixaram:
        print(id, end=" ")

print()