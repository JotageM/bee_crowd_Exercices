lista = []
num = int(input())
lista.insert(0,num)
while len(lista)<=9:
    print(lista)
    lista.append(num*2)
    num *= 2
for i in range(len(lista)):
    print(f"N{[i]} = {lista[i]}")

