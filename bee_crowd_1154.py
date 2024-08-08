idades = 0
casos = 0
while True:
    x = int(input())
    if x >= 0:
        idades += x
        casos += 1
    else:
        break
print(f"{(idades/casos):.2f}")
