#Exercício 5 e 6

#entrada

fruta = input("Digite o nome de uma fruta: \n")
fruta_valor = float(input("Digite o o preço da fruta: \n"))

legume = input("Digite o nome de uma legume: \n")
legume_valor = float(input("Digite o o preço da legume: \n"))

verdura = input("Digite o nome de uma verdura: \n")
verdura_valor = float(input("Digite o o preço da verdura: \n"))

print(fruta,": R$%2.2f"%fruta_valor)
print(legume,": R$%2.2f"%legume_valor)
print(verdura,": R$%2.2f"%verdura_valor)
