# Atividade 15 A - Ex 03 | Multiplicador

a = int(input('Digite um número inicial: '))
b = int(input('Digite um limite: '))

cont = 1
while cont <= b:
  print(f'{a} X {cont} = {a *cont}')
  cont +=1