notasList = []
aluno = [0, "", notasList]

print("Digite as notas ")

while aluno[0] <= 2:
  aluno[1] = input("Digite o nome do aluno: ")

  print(f"{"-"*50}\nInsira as notas bimestrais do aluno {aluno[1]}\n")

  for n in range(1, 5): # Realiza a coleta das notas e as insere na lista referente
    nota = float(input(f"Digite a nota do {n}° Bim: "))
    notasList.append(nota)

    while nota > 10:
      notasList.pop()
      nota = float(input(f"\n> Valor inválida!\n> Digite a nota do {n}° Bim do aluno {aluno[0]}: "))
      notasList.append(nota)
    
  media = sum(aluno[2]) / 4 # Faz a media da lista de notas

  if media >= 7.0:
    print(f"\n> O aluno {aluno[1]} foi APROVADO | Media = {media} \n> Notas: {aluno[2]} \n")
  else:
    print(f"\n> O aluno {aluno[1]} foi REPROVADO | Media = {media} \n> Notas: {aluno[2]} \n")

  # remove o nome do aluno e o intervalo de índices da lista de notas para repetir o primeiro laço após os condicionais
  aluno[1] = ""
  del notasList[0:5] 