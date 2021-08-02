
#função que retorna a nota
def entrada (msg):
    nota = int (input (msg))
    while nota < 0 or nota > 10:
        nota = int (input ("Nota inválida. Por favor, digite uma nota entre 0 e 10: "))
    return nota

#Funcao media
def media(n1, n2):
        return (n1*0.7 + n2*0.3)

#Funcao status
def status (media):
    if media >= 6:
        print("\nParabéns! Você foi aprovado! E sua média foi =", media)
    else:
        print("\nVocê está  REPROVADO! E sua média  foi =", media)

#Principal       
nota1 = entrada("Digite a 1a Nota: ")
nota2 = entrada("Digite a 2a Nota: ")

media_aluno = media(nota1,nota2)
print("\nMédia do aluno: ", media_aluno)
status(media_aluno)





