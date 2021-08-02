qde = 0
soma = 0
while qde < 5: #quero ler notas de 5 alunos
    nota = float(input("Digite sua nota N1 (0-10): "))
    while nota < 0 or nota > 10: #intervalo inválido
            nota = float(input("Nota inválida! Digite novamente: "))
    print("Nota do aluno",qde+1," = ",nota)
    qde = qde + 1
    soma = soma + nota

media = soma/5

print("A media da sala foi ",media)

