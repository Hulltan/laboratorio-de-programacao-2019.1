def total(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma 

n_pilha = int(input())
pedra_pilha = list(map(int, input().split()))
total_esperado = (n_pilha * (n_pilha + 1)) / 2
resultado = total(pedra_pilha) - total_esperado
if resultado % n_pilha == 0 and resultado >= 0:
  add = resultado / n_pilha
  termo = 1 + add
  somatorio = 0
  for i in range(n_pilha):
    somatorio += abs(pedra_pilha[i] - termo)
    termo += 1
  print(int(somatorio / 2))
else:
  print("-1")