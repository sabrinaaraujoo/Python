def pesoCalc(alt,sexo):
    if (sexo == "M"):
        peso = 72.7 * alt - 58
    if (sexo == "F"):
        peso = 62.1 * alt - 44.7
    return peso

alt = float(input("Digite a sua altura em metros: \n"))
sexo = input("Digite o seu sexo: (F para mulheres e M para homens \n)")



print("O seu preso ideal é:"peso)
