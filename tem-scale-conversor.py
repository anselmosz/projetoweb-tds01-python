# Atividade 15 A - Ex 01 | Calculadora de temperatura

temp = float(input('Informe uma temperatura: '))
finish = True

while finish:
  option = int(input('Escalas para conversão\n1 - Celcius\n2 - Fahrenheit\nSelecione uma escala: '))

  if option >=3:
    print('\n--------- Informe uma opção válida! ---------')

  elif option == 1:
    g = (temp *1.8) +32
    finish = False
    print(f'\nCelsius para Fahrenheit: {temp}°C -> {g}°F\n')
  elif option == 2:
    g = (temp -32) *(5/9)
    finish = False
    print(f'\nFahrenheit para Celsius: {temp}°F -> {g}°C\n')