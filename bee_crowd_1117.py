notas = 0
numeros = 0
while numeros < 2:
    num = float(input())
    if 0<= num <=10:
        numeros += 1
        notas += num
    else:
        print("nota invalida")
print(f"media = {(notas/2):.2f}")
