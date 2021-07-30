#calculando tempo da ampulheta

#Entrada

ampulheta1 = int(input("Quantos segundos tem a ampulheta maior? \n"))
ampulheta2 = int(input("Quantos segundos tem a ampulheta menor? \n"))

diferenca = ampulheta1 - ampulheta2
tempofinal = ampulheta1 + diferenca

#Saída

print("A diferença entre as ampulhetas é de: ",diferenca,"segundos")
print("Fazendo" ,ampulheta1,"+",diferenca,"se tem os",tempofinal,"segundos para o cozimento da erva.")
