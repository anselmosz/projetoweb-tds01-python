# Atividade 15 A - Ex 02 | Média

intervalo = int(input('> Digite um intervalo de números para somar: '))
print(f'Agora digite um intervalo de {intervalo} números')

total = 0
cont = 0

if cont != intervalo:

  while cont < intervalo:
    cont += 1

    nums = int(input(f'\nDigite o {cont}° número: '))
    total += nums

    media = total / intervalo

  print(f'\n-> A media aritimética de {total} em um intervalo de {intervalo} números é: {media}')

else: 
  print('\n---- Informe um intervalo de números válido! ----\n')