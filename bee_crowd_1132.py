num1 = int(input())
num2 = int(input())
soma = 0
if num2 > num1:
    for i in range(num1,num2 +1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(num2,num1 +1):
        if i % 13 != 0:
            soma += i
print(soma)
