n = int(input())
lista = []

marcados = 1
for _ in range(n):
    x = int(input())
    lista.append(x)

for i in range(len(lista)):
    if lista[i] != lista[i-1]:
        marcados+=1
print(marcados)



