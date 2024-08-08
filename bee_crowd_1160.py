t = int(input())
for i in range(t):
    anos = 0
    pa_, pb_, g1, g2= map(float,input().split())
    pa = int(pa_)
    pb = int(pb_)

    while pa<pb:
        crescimento_pa = pa * (g1/100)
        crescimento_pb = pb * (g2/100)
        pa += int(crescimento_pa)
        pb += int(crescimento_pb)
        anos +=1
    if anos>100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")




