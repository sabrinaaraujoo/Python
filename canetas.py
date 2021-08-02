#saida
print("Quantas canetas foram compradas?")
    #imprimindo na tela

#ENTRADA
qte_canetas = int(input())

print("qual foi o valor do troco?")
troco = int(input())

nota = int(input("com quanto você pagou?"))

valor_caneta = (nota - troco)/qte_canetas

print("custo de cada caneta =", valor_caneta)
