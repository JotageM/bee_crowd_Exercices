from math import sqrt, hypot
# while True:
#     try:
#         n = int(input())
#         h, c, l = map(int,input().split())
#         print(f"{((((sqrt((h**2) + (c**2))) * n) * l) /10000):.4f}")
#     except EOFError:
#         break
while True:
    try:
        n = int(input())
        h, c, l = map(int,input().split())
        print(f"{((hypot(h,c) * n * l)/10000):.4f}")
    except EOFError:
        break







