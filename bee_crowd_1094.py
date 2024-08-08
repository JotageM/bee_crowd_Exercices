num_of_test_cases = int(input())
coelhos= 0
ratos = 0
sapos = 0
for i in range(num_of_test_cases):
    amount,animal= input().split(" ")
    if animal == "C":
        coelhos += int(amount)

    elif animal == "S":
        sapos +=  int(amount)

    else:
        ratos +=  int(amount)
total = coelhos + ratos + sapos
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {((coelhos *100)/total):.2f} %")
print(f"Percentual de ratos: {((ratos *100)/total):.2f} %")
print(f"Percentual de sapos: {((sapos *100)/total):.2f} %")
