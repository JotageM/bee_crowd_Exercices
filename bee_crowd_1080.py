maior:int
posição = 0
for i in range(100):
    num= int(input())
    if num > maior:
        maior = num
        posição = i
print(maior)
print(posição +1)
