c = int(input())
t = input()
lista=[]
for i in range(12):
    lista.append([])
for i in range(12):
    for j in range(12):
        num = float(input())
        lista[i].append(num)
if t == "S":
    soma = 0

    for k in range(12):
        soma+=lista[k][c]
    print(f"{soma:.1f}")
if t == "M":
    media = 0
    soma = 0

    for k in range(12):
        soma +=lista[k][c]
    media = soma/12
    print(f"{media:.1f}")

