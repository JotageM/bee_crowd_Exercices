operation = input()

soma = 0
contador = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if i < j and (i<12 -j -1):
            soma += x
            contador +=1
if operation == "S":
    print(f"{soma:.1f}")
else:
    print(f"{(soma/contador):.2f}")







