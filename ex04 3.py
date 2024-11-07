# Atividade 13 - Exercício 04 | Urna
eleitor = 1
repeat = True

option = int(input(f'Olá Eleitor N°{eleitor} | Selecione uma opção\n1. Jair Rodrigues\n2. Carlos Luz\n3. Neves Rocha\n4. Nulo\n5. Branco\nDigite uma opção: '))

jair = 0
carlos = 0
neves = 0
nulo = 0
branco = 0
# ---------------------------------------------------------------------------------------------- #
while repeat == True and option != 6:
  eleitor += 1

  if option > 5 or option < 1:
    eleitor -= 1
    print('\n> Opção inválida! Informe uma opção entre 1 e 5\n')
    option

  if option == 1:
    jair += 1
  elif option == 2:
    carlos += 1
  elif option == 3:
    neves += 1
  elif option == 4:
    nulo += 1
  elif option == 5:
    branco += 1

  option = int(input(f'-\nOlá Eleitor N°{eleitor} | Selecione um candidato\n1. Jair Rodrigues\n2. Carlos Luz\n3. Neves Rocha\n4. Nulo\n5. Branco\nDigite uma opção: '))
# ---------------------------------------------------------------------------------------------- #
  if option == 6:
    eleitor -= 1
    repeat = False
    
    total = jair +carlos +neves +nulo +branco
    nuloPrc = (nulo / total) * 100
    brancoPrc = (branco / total) * 100
    
    print(f'\nA quantidade total de votos apurados nesta urna foi de: {total}\n- Eleitores: {eleitor}\n- Jair Rodrigues: {jair}\n- Carlos Luz: {carlos}\n- Neves Rocha: {neves}\n- Votos nulos: {nulo} - {nuloPrc}%\n- Votos brancos: {branco} - {brancoPrc}%\n')

    if jair > carlos and jair > neves and jair > nulo and jair > branco:
      print(f'O vencedor foi Jair Rodrigues, com um total de {jair} votos')

    elif carlos > jair and carlos > neves and carlos > nulo and carlos > branco:
      print(f'O vencedor foi Carlos Luz, com um total de {carlos} votos')

    elif neves > jair and neves > carlos and neves > nulo and neves > branco:
      print(f'O vencedor foi Neves Rocha, com um total de {neves} votos')
    else:
      print('nenhum candidato foi eleito')