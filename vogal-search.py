caracteres = []

for c in range(10):
  letra = input('Digite uma letra: ')
  
  if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
    caracteres.append(letra.upper())
  
print(f"As consoantes são: {caracteres} | O total de consoantes é: {len(caracteres)}")