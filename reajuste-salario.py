qtde_empregados = 0
soma = 0
media = 0
num_homem = 0
num_mulheres = 0
porc = 0

n = int(input("Quantos empregados são? \n"))
todos = n

while (n >= 1):
    nome = input("\nDigite o nome: \n")
    
    sexo = input("Digite o sexo: (somente F para feminino ou M para masculino) \n").upper()
    while (sexo != "F" and sexo != "M"):
        sexo = input("Sexo inválido! \nDigite novamente: \n").upper()
        
    salario = float(input("Digite o valor do salário: (A partir de R$850,00)\n"))
    while (salario < 850):
        salario = float(input("Valor inválido! \nDigite novamente: \n"))

    if (salario >= 3000):
        acres = salario * 0.045
        total = salario + acres
        print("O salário de",nome,"teve um acrescimo de R$%4.2f"%acres,"Total: R$%4.2f"%total)

    if (salario < 3000 and salario >= 2000):
        acres = salario * 0.065
        total = salario + acres
        qtde_empregados +=1
        print("O salário de",nome,"teve um acrescimo de R$%4.2f"%acres,"Total: R$%4.2f"%total)
        
    if (salario < 2000):
        acres = salario * 0.085
        total = salario + acres
        print("O salário de",nome,"teve um acrescimo de R$%4.2f"%acres,"Total: R$%4.2f"%total)

    if (sexo == "M"):
        num_homem +=1
        soma = soma + total
        media = soma / num_homem
        
    if (sexo == "F"):
        num_mulheres +=1
        porc = (num_mulheres * 100) / todos

    n = n - 1

print("\nA quantidade de empregados que receberam o reajuste de 6,5% é de",qtde_empregados)
print("O salário reajustado médio entre os empregados do sexo masculino é de: R$%4.2f"%media)
print("O percentual de empregados do sexo feminino entre o total de empregados é de:",porc,"%")
