n = int(input())
odds = []
even =[]
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odds.append(number)
odds.sort(reverse=True)
even.sort()
for i in even:
    print(i)
for i in odds:
    print(i)



