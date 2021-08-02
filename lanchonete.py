'''
Nome: Sabrina de Santana Araujo TIA:32108265
'''

#Entrada
print("Côdigo   Especificação    Preço")
print("  1      Cachorro Quente  R$4.00")
print("  2      X-Salada         R$4.50")
print("  3      X-Bacon          R$5.00")
print("  4      Torrada simples  R$2.00")
print("  5      Refrigerante     R$1.50")

cod = int(input("Digite o côdigo do que deseja: (apenas números)\n"))
qtd = int(input("Digite a quantidade do produto: (somente números)\n"))

total = 0

#proccessamento
if (cod == 1):
    total = qtd * 4
elif (cod == 2):
    total = qtd * 4.50
elif (cod == 3):
    total = qtd * 5
elif (cod == 4):
    total = qtd * 2
elif (cod == 5):
    total = qtd * 1.50
else:
    print("Digite somente o côdigo de números representados na tabela.")

#Saída
print("Total: R$%2.2f"%total)
