while True:
  n_linha, n_coluna, n_instrucao = list(map(int, input().split()))
  if n_linha == n_coluna == 0:
    break
  linha = [0] * n_coluna
  matriz = [linha] * n_linha
  n, l, s, o = 0, 1, 2, 3
  count_figurinha = 0
  for i in range(n_linha):
    matriz[i] = list(input())
  instrucao = input()
  for i in range(n_linha):
    for j in range(n_coluna):
      #Define a posicao inicial do robo
      if matriz[i][j] == 'N' or matriz[i][j] == 'L' or matriz[i][j] == 'S' or matriz[i][j] == 'O':
        posicao_linha_robo = i
        posicao_coluna_robo = j
        #Define a direcao inicial do robo
        if matriz[i][j] == 'N':
          direcao_robo = n
        elif matriz[i][j] == 'L':
          direcao_robo = l
        elif matriz[i][j] == 'S':
          direcao_robo = s
        else:
          direcao_robo = o
  #Executa instrucoes
  for instrucao_i in range(n_instrucao):
    #Caso o robo deva se mover
    if instrucao[instrucao_i] == 'F':
      #Norte
      if direcao_robo == 0:
        if posicao_linha_robo > 0 and matriz[posicao_linha_robo - 1][posicao_coluna_robo] != '#':
          posicao_linha_robo -= 1
          if matriz[posicao_linha_robo][posicao_coluna_robo] == '*':
            count_figurinha += 1
            matriz[posicao_linha_robo][posicao_coluna_robo] = '.'
      #Leste
      elif direcao_robo == 1:
        if posicao_coluna_robo < n_coluna - 1 and matriz[posicao_linha_robo][posicao_coluna_robo + 1] != '#':
          posicao_coluna_robo += 1
          if matriz[posicao_linha_robo][posicao_coluna_robo] == '*':
            count_figurinha += 1
            matriz[posicao_linha_robo][posicao_coluna_robo] = '.'
      #Sul
      elif direcao_robo == 2:
        if posicao_linha_robo < n_linha - 1 and matriz[posicao_linha_robo + 1][posicao_coluna_robo] != '#':
          posicao_linha_robo += 1
          if matriz[posicao_linha_robo][posicao_coluna_robo] == '*':
            count_figurinha += 1
            matriz[posicao_linha_robo][posicao_coluna_robo] = '.'
      #Oeste
      else:
        if posicao_coluna_robo > 0 and matriz[posicao_linha_robo][posicao_coluna_robo - 1] != '#':
        if posicao_coluna_robo > 0 and matriz[posicao_linha_robo][posicao_coluna_robo - 1] != '#':
          posicao_coluna_robo -= 1
          if matriz[posicao_linha_robo][posicao_coluna_robo] == '*':
            count_figurinha += 1
            matriz[posicao_linha_robo][posicao_coluna_robo] = '.'
    #Caso o robo altere sua direcao
    else:
      #Direita
      if instrucao[instrucao_i] == 'D':
        direcao_robo += 1
        if direcao_robo > 3:
          direcao_robo = 0
      #Esquerda
      else:
        direcao_robo -= 1
        if direcao_robo < 0:
          direcao_robo = 3
  print(count_figurinha)