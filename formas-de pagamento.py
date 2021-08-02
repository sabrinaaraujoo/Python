'''
Nome:Sabrina de Santana Araujo TIA:32108265 Turma:01N11

Exercício 2

'''

#Entrada

preco = float(input("Qual é o preço da etiqueta?\n"))

print("\nDigite 1 para: Á vista dinheiro ou cheque, recebe 10% de desconto")
print("Digite 2 para: Á vista no cartão de crédito, recebe 5% de desconto")
print("Digite 3 para: Em 2 vezes, preço normal de etiqueta sem juros")
print("Digite 4 para: Em 3 vezes, preço normal de etiqueta mais juros de 10%\n")

formapag = int(input("Qual a forma de pagamento?\n"))

desc = 0
parc = 0
juros = 0
total = 0

#Processamento
if (formapag == 1):
    desc = preco * 0.1
    total = preco - desc
    print("\nVocê recebeu 10% de desconto!")
elif (formapag == 2):
    desc = preco * 0.05
    total = preco - desc
    print("\nVocê recebeu 5% de desconto!")
elif (formapag == 3):
    parc = preco / 2
    total = preco
    print("\nVocê parcelou 2 vezes sem juros.")
elif(formapag == 4):
    juros = preco * 0.1
    total = preco + juros
    parc = total / 3
    print("\nVocê parcelou 3 vezes com juros de 10%.")
else:
    print("Digite apenas 1/2/3/4 para forma de pagamento.")

#saida

print("\n=========== Nota: ============")
print("Forma de pagamento:",formapag)
print("Preço da etiqueta:. R$%2.2f"%preco)
print("Desconto:.......... R$%2.2f"%desc)
print("Juros:............. R$%2.2f"%juros)
print("Valor da parcela:.. R$%2.2f"%parc)
print("Total:............. R$%2.2f"%total)
    
