n= int(input())
gasolina = 0
alcool = 0
diesel = 0
while n != 4:
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1

    n= int(input())
    while n not in(1,2,3,4):
        n=int(input())




print(f"MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")