

while True:
    try:
        m,n = map(int,input().split())
        fatorial_n = 1
        for i in range(1,n+1):
            fatorial_n *= i
        fatorial_m=1
        for i in range(1,m+1):
            fatorial_m *= i
        print(fatorial_m + fatorial_n)
    except EOFError:
        break

