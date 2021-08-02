#Entradas

sal_hora = float(input("Quanto você ganha por hora? \n"))

num_hr = int(input("Quantas horas você trabalhou? \n"))

salario = sal_hora * num_hr

sind = (salario * 3) / 100

fgts = (salario * 11) / 100

print("Salário Bruto: ",sal_hora,"*",num_hr,"  R$ %4.2f" %salario)
print("Para o sindicato: R$",sind)
print("Para o FGTS: R$",fgts)

if (salario > 2500):
    resul1 = (salario * 20) / 100
    print("(-) IR (20%): R$",resul1)
    desc1 = salario - resul1 - sind
    print("Valor liquido: R$",desc1)
    
elif (salario > 1500 or salario == 2500):
    resul2 = (salario * 10) / 100
    print("(-) IR (10%): R$",resul2)
    desc2 = salario - resul2 - sind
    print("Valor liquido: R$",desc2)
    
elif (salario > 900 or salario == 1500):
    resul3 = (salario * 5) / 100
    print("(-) IR (5%): R$",resul3)
    desc3 = salario - resul3 - sind
    print("Valor liquido: R$",desc3)
    
elif (salario < 900 or salario == 900):
    desc4 = salario - sind
    print("Isento!")
    print("Valor liquido: R$",desc4)






