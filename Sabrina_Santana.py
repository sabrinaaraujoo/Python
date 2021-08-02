'''
Nome:Sabrina de Santana Araujo TIA:32108265 

'''

#Entrada

preco = float(input("Qual é o preço da etiqueta?\n"))
qtd = int(input("Digite a quantidade desejada:\n"))

print("\nDigite 1 para: Á vista dinheiro ou cheque, recebe 10% de desconto")
print("Digite 2 para: Á vista no cartão de crédito, recebe 5% de desconto")
print("Digite 3 para: Em 2 vezes, preço normal de etiqueta sem juros")
print("Digite 4 para: Em 3 vezes, preço normal de etiqueta mais juros de 10%\n")

formapag = int(input("Qual a forma de pagamento?\n"))

desc = 0
juros = 0
subtotal = preco*qtd

#Processamento
if (formapag == 1):
    desc = subtotal * 0.1
    total = subtotal - desc
elif (formapag == 2):
    desc = subtotal * 0.05
    total = subtotal - desc
elif (formapag == 3):
    total = subtotal
elif(formapag == 4):
    juros = subtotal * 0.1
    total = subtotal + juros
else:
    print("Valor total da compra é de R$%2.2f"%total)
    print("Digite apenas 1/2/3/4 para forma de pagamento.")

#Saída

print("Valor total da compra é de R$%2.2f"%total)

    
