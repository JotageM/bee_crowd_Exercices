x1,y1,x2,y2= map(int,input().split())
while x1 != 0 or x2 != 0 or y1 != 0 or y2 != 0:
    mov = 0
    if x1 == x2 and y1 == y2:
        print(mov)
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        print(mov +1)
    else:
        print(mov+2)
    x1,y1,x2,y2= map(int,input().split())

