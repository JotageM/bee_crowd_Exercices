x,y= list(map(int,input().split()))
while not(x==y):
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
    x,y= list(map(int,input().split()))
