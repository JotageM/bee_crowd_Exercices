num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
lista_nums = [num1,num2,num3,num4,num5,num6]
positivos = 0
for num in lista_nums:
    if num > 0:
        positivos+= 1
print(f"{positivos} valores positivos")
