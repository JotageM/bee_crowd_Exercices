def func_Rafael(x,y):
    return ((3*x)**2 + (y**2))


def func_Beto(x,y):
    return (2 *(x**2) + (5*y) ** 2)


def func_Carlos(x,y):
    return ((-100*x) + (y **3))





n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    if  func_Beto(x,y) < func_Rafael(x,y) > func_Carlos(x,y):
        print("Rafael ganhou")
    elif func_Rafael(x,y) < func_Beto(x,y) > func_Carlos(x,y):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")