while True:
  try:
    n_digito, n_apagar = list(map(int, input().split()))
    numero = input()
    novo_numero = ''
    n_retirar = n_digito - n_apagar
    aux = 0
    inicio = 0
    fim = n_digito - n_retirar
    while n_digito - n_apagar > len(novo_numero):
      atual = 0
      for i in range(inicio, fim + 1):
        if int(numero[i]) > atual:
          atual = int(numero[i])
          aux = i
      novo_numero += str(atual) 
      n_retirar -= 1
      inicio = aux + 1
      fim  = n_digito - n_retirar
    print(novo_numero)
  except EOFError:
    break