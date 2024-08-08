n = int(input())
for i in range(n):
    x = float(input())
    dias = 0
    while x > 1:
        x/=2
        dias += 1
    print(f"{dias} dias")