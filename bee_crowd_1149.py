
valores = input().split()
a = int(valores[0])
ultimo_numero = len(valores) - 1
n = int(valores[ultimo_numero])


soma = 0
for _ in range(n):
    soma += a
    a += 1
print(soma)



