# Dado 2 números inteiros, calcular a soma, diferenca, produto e divisao


#função que retorna o número do menu
def menu ():
    n = int (input ("\nEscolha a opção desejada:"
                    "\n1 - Adição"
                    "\n2 - Subtração"
                    "\n3 - Multiplicacao"
                    "\n4 - Divisão"
                    "\n0 - Sair"
                    "\n\nOpção desejada: "))
    while n<0 or n>4:
        n = int (input ("Opção inválida. Por favor, digite um número entre 1 e 4 ou 0 para sair: "))
    return n


#Funcao soma
def soma(n1, n2):
    return n1+n2

#Funcao diferenca
def diferenca(n1, n2):
    return n1-n2

#Funcao produto
def produto(n1, n2):
    return n1*n2

#Funcao divisao
def divisao(n1, n2):
    if n2!=0:
        return n1/n2
    else:
        return "Não é possivel fazer divisão por zero"


#Principal
a = int (input ("Digite um número inteiro: "))
b = int (input ("Digite outro número inteiro: "))

while True:
    opcao = menu()

    if opcao == 0:
        break

    if opcao == 1:
        print ("\nResultado da soma = ", soma(a,b))
    elif opcao == 2:
        print ("\nResultado da subtração = ", diferenca(a,b))
    elif opcao == 3:
        print ("\nResultado da multiplicação = ", produto(a,b))
    elif opcao == 4:
        print ("\nResultado da divisão = ", divisao(a,b))
    else:
        print("Opção inválida")

#print("Boa noite))
