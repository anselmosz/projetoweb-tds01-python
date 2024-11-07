'''
Fazer um programa que leia um vetor de 5 nums int, e em seguida realize a soma e multiplicação entre os mesmos
'''

vetorList = []

for i in range(1,6):
  n = int(input(f"Digite o {i}° número: "))
  vetorList.append(n)

numSoma = sum(vetorList)

numMult = numSoma * len(vetorList)  

print(f"{"-"*50}\n> Números no vetor: {vetorList}\n{"-"*50}\n> Soma dos números no vetor: {numSoma}\n> Multiplicação do total dos números pelo tamanho do vetor: {numMult}")