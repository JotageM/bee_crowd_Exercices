n = int(input())
cities = 1

while n != 0:
    dicionario = {}
    pessoas = 0
    consumo = 0
    
    for _ in range(n):
        x, y = map(int, input().split())
        result = y // x
        pessoas += x
        consumo += y
        
        dicionario[result] = dicionario.get(result, 0) + x

    listaordenada = sorted(dicionario.items())
    media = consumo / pessoas
    
    if cities > 1:
        print("")
    
    print(f"Cidade# {cities}:")
    print(' '.join(f"{v}-{k}" for k, v in listaordenada))
    print(f"Consumo medio: {media:.2f} m3.")
    
    n = int(input())
    cities += 1





