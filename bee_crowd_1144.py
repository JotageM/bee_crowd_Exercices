n=int(input())
a = 1
for i in range(n):
    print(f"{a} {a**2} {a**3}")
    print(f"{a} {(a**2)+1} {(a**3)+1}")
    a += 1
