linha, coluna, sub_linha, sub_coluna = list(map(int, input().split()))
a = [0]  * (coluna + 1)
entrada = [a] * (linha + 1)
c = [0]  * (coluna + 1)
pomar = [c] * (linha + 1)
maior = 0
k = sub_linha 
l = sub_coluna 
for i in range(linha):
  b = list(map(int, input().split()))
  entrada[i + 1] = [0] + b
  pomar[i + 1] = [0] * (coluna + 1)
for i in range(1, linha + 1):
  for j in range(1, coluna + 1):
    pomar[i][j] = pomar[i - 1][j] + pomar[i][j - 1] - pomar[i - 1][j - 1] + entrada[i][j]
while k < linha + 1:
  while l < coluna + 1:
    d = pomar[k][l] - pomar[k][l - sub_coluna] - pomar[k - sub_linha][l] + pomar[k - sub_linha][l - sub_coluna]
    if d > maior:
      maior = d
    l += 1
  k += 1
  l = sub_coluna
print(maior)
