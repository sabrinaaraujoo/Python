#resultado


def pes(feet):
        conver_pes_m = feet * 3.281
        print("\nmetros: ", conver_pes_m)
        return(conver_pes_m)


#programa principalqtade de pés

vlr_pes = int(input("Digite a quantidade de pés: "))

print("\n",vlr_pes)
                
resposta = pes(vlr_pes)

print("A qtde de pés é: ", resposta)
