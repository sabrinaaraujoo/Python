#maior de dois numeros

ano = int(input("Digite o ano do carro:\n"))

preco = float(input("Digite o preço do carro: R$"))

if ( ano < 2010):
    pgto = preco * 0.025
    print("O ano do carro:",ano,"\nPreço do carro: R$%5.2f"%preco,"\nTaxa cobrada antes de 2010 é 2,5%","\nPagamento com a taxa: R$%.2f"%pgto)
else:
    pgto = preco * 0.035
    print("O ano do carro:",ano,"\nPreço do carro: R$%5.2f"%preco,"\nTaxa cobrada depois de 2010 é 3,5%","\nPagamento com a taxa: R$%.2f"%pgto)


