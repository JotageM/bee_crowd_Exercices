
m,n=list(map(int,input().split()))
while m>0 and n>0:
    soma = 0
    lista = []
    a = min(m, n)
    b = max(m, n)
    for i in range(a,b+1):
        lista.append(i)
        soma +=i
    print(f"{' '.join([str(lista[i]) for i in range(len(lista))])} Sum={soma}")

    m,n=list(map(int,input().split()))