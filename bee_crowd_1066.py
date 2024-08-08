num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
lista_nums= [num1,num2,num3,num4,num5]
pares = 0
impares = 0
positivos = 0
negativos = 0
for num in lista_nums:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")



