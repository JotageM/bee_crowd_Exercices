from math import gcd
from mdc import mdc

n = int(input())
for i in range (n):
    f1, f2 = map(int,input().split())
    print(mdc.mdc(f1,f2))


