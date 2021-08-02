'''
Nome:Sabrina de Santana Araujo TIA:32108265 Turma:01N11

Exercício 2

'''

#Entrada

cont = 0

n = int(input("Digite a quantidade de pessoas: (minímo 1 e máximo 50) \n"))

while (1 <= n <=50):
    altura = float(input("Qual a sua altura em metros? \n"))
    if (altura < 1.30 or altura > 2.30):
        print("Altura inválida!")
        altura = float(input("Qual a sua altura em metros? \n"))
        sexo = input("Qual o seu sexo? Digite F para feminino ou M para masculino. \n").upper()
    cont +1
