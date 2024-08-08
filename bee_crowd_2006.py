n = int(input())
guess = [int(i) for i in input().split()]
palpites_certos = 0
for i in range(len(guess)):
    if guess[i] == n:
        palpites_certos += 1
print(palpites_certos)


