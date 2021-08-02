#Pneu

#entradas
pdesejada = int(input("Entre com a pressão desejada entre 1 e 40: \n"))

plida = int(input("entre com a pressão lida pela BOMBA, entre 1 e 40: \n"))

valorpressao = pdesejada - plida

#processamento

if (pdesejada > plida):
    print("Precisa ENCHER o pneu, falta(m):", valorpressao,"PSI")
elif (pdesejada == plida):
    print("Não precisa encher o pneu!", valorpressao,"PSI")
else:
    print("Precisa ESVAZIAR o pneu, em ", valorpressao,"PSI")

