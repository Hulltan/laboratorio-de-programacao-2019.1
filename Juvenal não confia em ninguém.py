def kira(matriz, l, c, mark):
  matriz[l][c] = mark
  if c - 1 >= 0 and matriz[l][c - 1] == "#":
    matriz[l][c - 1] = mark
    kira(matriz, l, c - 1, mark)
  if l + 1 < linha and matriz[l + 1][c] == "#":
    matriz[l + 1][c] = mark
    kira(matriz, l + 1, c, mark,)
  if c + 1 < coluna and matriz[l][c + 1] == "#" :
    matriz[l][c + 1] = mark
    kira(matriz, l, c + 1, mark)
  if l - 1 >= 0 and matriz[l - 1][c] == "#":
    matriz[l - 1][c] = mark
    kira(matriz, l - 1, c, mark)



linha, coluna = list(map(int, input().split()))
count = 0
p = [0] * coluna
mapa = [p] * linha
ship = []
vetor = []
mark = 0
for i in range(linha):
  n = list(input())
  mapa[i] = n
for i in range(linha):
  for j in range(coluna):
    if mapa[i][j] == "#":
      kira(mapa, i, j, mark)
      mark += 1
vetor = [0] * mark
for i in range(linha):
  for j in range(coluna):
    if mapa[i][j] != ".":
      vetor[mapa[i][j]] += 1
n_shot = int(input())
shot = [0] * 2
for i in range(n_shot):
  shot = list(map(int, input().split()))
  if mapa[shot[0] - 1][shot[1] - 1] != '.':
    vetor[mapa[shot[0] - 1][shot[1] - 1]] -= 1
size = len(vetor)
for i in range(size):
  if vetor[i] == 0:
    count += 1
print(count)






