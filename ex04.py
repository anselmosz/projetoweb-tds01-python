# Atividade 15 A - Ex04 | Pirâmide numérica

numBase = int(input('Digite um número: '))

cont1 = 0

while cont1 < numBase:
  numLinha = ''
  cont1 += 1
  cont2 = 1

  while cont2 <= cont1:
    numLinha += str(cont2) + ' '
    cont2 += 1
  print(numLinha)