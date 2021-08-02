'''
4. Escreva um procedimento que receba um número inteiro e imprima o mês correspondente ao

número. Por exemplo, 2 corresponde à “fevereiro”. O procedimento deve mostrar uma mensagem

de erro caso o número recebido não faça sentido. Gere também um algoritmo que leia um valor

como entrada do usuário e chame o procedimento criado.
'''

#validação
def entrada(msg):
    num = int(input (msg))
    while num < 1 or num > 12:
        num = int(input("Valor Inválido! Digite apenas nímeros correspondentes aos meses! \n"))
    return num

#Mês correspondentes
def meses (m):
    if m == 1:
        print("O mês correspondente é Janeiro!")
    elif m == 2:
        print("O mês correspondente é Fevereiro!")
    elif m == 3:
        print("O mês correspondente é Março!")
    elif m == 4:
        print("O mês correspondente é Abril!")
    elif m == 5:
        print("O mês correspondente é Maio!")
    elif m == 6:
        print("O mês correspondente é Junho!")
    elif m == 7:
        print("O mês correspondente é Julho!")
    elif m == 8:
        print("O mês correspondente é Agosto!")
    elif m == 9:
        print("O mês correspondente é Setembro!")
    elif m == 10:
        print("O mês correspondente é Outubro!")
    elif m == 11:
        print("O mês correspondente é Novembro!")
    else:
        print("O mês correspondente é Dezembro!")

mes = entrada("Digite um mês: (Somente numeros)\n")

resp = meses(mes)

        
