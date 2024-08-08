a=int(input())
b=int(input())
aux = a
if (a > b):
    a = b
    b = aux
while (a < b):
    a += 1
    if (a % 5 == 2 or a % 5 == 3 and a != b):
        print(a)




