x = int(input())
while x != 0:
    lista = []
    for i in range(1,x+1):
        lista.append(i)
    print(*lista)
    x = int(input())

