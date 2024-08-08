x,y=list(map(int,input().split()))
while x != 0 and y!=0:
    if x>0 and y>0:
        print("primeiro")
    elif x>0 and y<0:
        print("quarto")
    elif x<0 and y>0:
        print("segundo")
    else:
        print("terceiro")
    x,y=list(map(int,input().split()))
