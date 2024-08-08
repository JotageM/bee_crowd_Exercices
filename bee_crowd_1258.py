aux= False
while True:
    n = int(input())
    if n == 0:
        break

    camisas = []

    for _ in range(n):
        nome = input()
        cor, tam= input().split()
        camisas.append((nome, cor, tam))


    camisas.sort(key=lambda x: (x[1], -ord(x[2]), x[0]))

    for cor in ["branco", "vermelho"]:
        for tam in ["P", "M", "G"]:
            for nome in camisas:
                if nome[1] == cor and nome[2] == tam:
                    print(f"{cor} {tam} {nome[0]}")

    print()


