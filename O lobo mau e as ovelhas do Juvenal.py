
def kira(matriz, l, c, mark, lobo, ovelha):
  listaCheck = ['v','k','.']
  if matriz[l][c] == 'k':
    ovelha[mark] += 1 
  elif matriz[l][c] == 'v':
    lobo[mark] += 1
  matriz[l][c] = mark
  if c - 1 >= 0 and matriz[l][c - 1] in listaCheck:
    if matriz[l][c - 1] == 'k':
      ovelha[mark] += 1 
    elif matriz[l][c - 1] == 'v':
      lobo[mark] += 1
    matriz[l][c - 1] = mark
    kira(matriz, l, c - 1, mark, vet_lobo, vet_ovelha)
  if l + 1 < linha and matriz[l + 1][c] in listaCheck:
    if matriz[l + 1][c] == 'k':
      ovelha[mark] += 1 
    elif matriz[l + 1][c] == 'v':
      lobo[mark] += 1
    matriz[l + 1][c] = mark
    kira(matriz, l + 1, c, mark, vet_lobo, vet_ovelha)
  if c + 1 < coluna and matriz[l][c + 1] in listaCheck:
    if matriz[l][c + 1] == 'k':
      ovelha[mark] += 1 
    elif matriz[l][c + 1] == 'v':
      lobo[mark] += 1
    matriz[l][c + 1] = mark
    kira(matriz, l, c + 1, mark, vet_lobo, vet_ovelha)
  if l - 1 >= 0 and matriz[l - 1][c] in listaCheck:
    if matriz[l - 1][c] == 'k':
      ovelha[mark] += 1 
    elif matriz[l - 1][c] == 'v':
      lobo[mark] += 1
    matriz[l - 1][c] = mark
    kira(matriz, l - 1, c, mark, vet_lobo, vet_ovelha)

linha, coluna = list(map(int, input().split()))
p = [0] * coluna
mapa = [p] * linha
mark = 0
vet_lobo = []
vet_ovelha = []
count_lobo = 0
count_ovelha = 0
for i in range(linha):
  n = list(input())
  mapa[i] = n
for i in range(linha):
  for j in range(coluna):
    if mapa[i][j] == 'v' or mapa[i][j] == "k": 
      vet_lobo.append(0)
      vet_ovelha.append(0)
      kira(mapa, i, j, mark, vet_lobo, vet_ovelha)
      mark += 1
size_ovelha = len(vet_ovelha)
for i in range(size_ovelha):
  if vet_ovelha[i] > vet_lobo[i]:
    count_ovelha += vet_ovelha[i]
  else: 
    count_lobo += vet_lobo[i]
print("%d %d" % (count_ovelha, count_lobo))
