'''
Exercício 11

Nome:Sabrina de Santana Araujo TIA:32108265 Turma:01N11

'''

#Entrada

kg = int(input("Quantos quilos você pescou hoje?\n"))

if (kg > 50):
    diferenca = kg - 50
    multa = diferenca * 4
    print("Você excedeu Kg",diferenca,"terá que pagar uma multa de R$%2.2f"%multa)
else:
    print("Dentro do Regulamento.")
