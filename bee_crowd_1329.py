n = int(input())
while n > 0:
    x =[int(i) for i in input().split()]
    mary = 0
    john = 0
    for i in range(len(x)):
        if x[i] == 0:
            mary += 1
        else:
            john += 1
    print(f"Mary won {mary} times and John won {john} times")
    n = int(input())


