n = 100
soma = 0
qtd_otimo = 0
qtd_ruim = 0
maior = 0
media = 0
qtd_pessimo = 0
porcentagem = 0
dec = 0
menor_c = 0
menor_d = 0
dif = 0

while (1 <= n <=10):
    idade = int(input("Quantos anos você tem? (minímo 14 anos) \n"))
    while (idade < 14):
        idade = int(input("Idade não permitidade! Digite novamente:(minímo 14 anos) \n"))

    print("Nota | Significado")
    print("  A  | Ótimo")
    print("  B  | Bom")
    print("  C  | Regular")
    print("  D  | Ruim")
    print("  E  | Péssimo")

    opn = input("Qual a sua nota para o filme? (Somente letras!) \n").upper()
    while (opn != "A" and opn != "B" and opn != "C" and opn != "D" and opn != "E"):
        opn = input("Resposta inválida! \n Digite novamente:(Somente letras!) \n").upper()
    
    if (opn == "A"):
        qtd_otimo +=1

    if (opn == "D"):
        qtd_ruim +=1
        soma = soma + idade
        media = soma / qtd_ruim

    if (opn == "E"):
        qtd_pessimo +=1
        dec = qtd_pessimo / 10
        porcentagem = dec * 100
        
    if (opn == "B"):
        maior = idade
        if (idade > maior):
            maior = idade
            
    if (opn == "C"):
        menor_c = idade
        if (idade < menor_c):
            menor_c = idade
            
    if (opn == "D"):
        menor_d = idade
        if (idade < menor_d):
            menor_d = idade
            
    dif = menor_c - menor_d
    n = n - 1 

print("A quantidade de respostas Ótimo:",qtd_otimo)
print("A média de idade das pessoas que responderam Ruim:",media)
print("A porcentagem de respostas Péssimo:",porcentagem,"%")
print("A maior idade entre as pessoas que responderam Bom:",maior)
print("a diferença entre a menor idade que respondeu Regular e a menor idade que respondeu Ruim:",dif)
