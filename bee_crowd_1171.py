
# n = int(input())
# lista = []
# for i in range(n):
#     x = int(input())
#     lista.append(x)
# lista.sort()
# lista_unica = list(set(lista))
# print(lista)
# print(lista_unica)
n = int(input())
lista = {}
for i in range(n):
	x = int(input())
	if(x in lista):
		lista[x] += 1
	else:
		lista[x] = 1


chaves = lista.keys()
chaves = sorted(chaves)

for k in chaves:
	print("%d aparece %d vez(es)" %(k,lista[k]))








