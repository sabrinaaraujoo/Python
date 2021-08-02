soma = 0
numerador = 1
for denominador in range(1,51,1):
  print(numerador,"/",denominador)
  soma = soma + numerador/denominador
  numerador += 2

print("\nSoma =",soma)
