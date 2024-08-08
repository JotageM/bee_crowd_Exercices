n = int(input())
fruits_list = {}

for i in range(n):
    totalprice = 0
    m = int(input())
    for i in range(m):
        fruit,price = input().split()
        fruits_list[fruit] = price
    p = int(input())
    for i in range(p):
        fruit,quantity = input().split()
        if fruit in fruits_list.keys():
            totalprice += int(quantity) * float(fruits_list[fruit])
    print(f"R$ {totalprice:.2f}")


print(fruits_list)
