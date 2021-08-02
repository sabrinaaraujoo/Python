
n = int(input("Digite a quantidade de pessoas que deseja cadastrar: (minimo 1 e maximo 50) \n"))

num_homem = 0
num_mulher = 0
maior = 0
menor = 0
soma = 0
media = 0

while(1 <= n <= 50):
    altura = float(input("Qual a altura da pessoa? \n"))
    while (altura < 1.00 or altura > 2.30):
        altura = float(input("Altura inválida! \n Qual a altura da pessoa? \n"))
        
    sexo = input("Qual o sexo da pessoa? (apenas F ou M) \n").upper()
    while (sexo != "F" and sexo != "M"):
        sexo = input("Sexo inválido! \n Qual o sexo da pessoa? (apenas F ou M) \n").upper()
    cont = n - 1
    
    if (n == 1):
        maior = menor = altura
    else:
        if (altura > maior):
            maior = altura
        if (altura < menor):
            altura = menor

    if (sexo == "F"):
        num_mulher +=1
        soma = soma + altura
        media = soma / num_mulher
    
    if (sexo == "M"):
        num_homem +=1
    
print("A maior altura do grupo é:",maior)
print("A menor altura do grupo é:",menor)
print("A média de altura de mulheres é:",media)
print("A quantidade de homens no grupo é:",num_homem)
