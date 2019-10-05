n_fatias = int(input())
pizza = list(map(int, input().split()))
fatias = pizza + pizza[:-1]
inicio = 0
fim = n_fatias
total = 0
quantidade = [0] 
lista = [0] * n_fatias
aux = 0
for i in range(n_fatias):
    for j in range(inicio, fim):
        if fatias[j] + quantidade[aux] > 0:
            quantidade[aux] += fatias[j]
        else:
            quantidade += [0]
            aux += 1
    inicio += 1
    fim += 1
    lista[i] = max(quantidade)
    quantidade = [0]
    aux = 0
if max(lista) > 0:
    print(max(lista))
else:
    print('0')
