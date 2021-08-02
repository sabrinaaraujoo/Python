#crime

#entrada

p_a = int(input("Telefonou para a vítima? 1-SIM ou 0-NÃO: \n"))

p_b = int(input("Esteve no local do crime? 1-SIM ou 0-NÃO: \n"))

p_c = int(input("Mora perto da vítima? 1-SIM ou 0-NÃO: \n"))

p_d = int(input("Devia para a vítima? 1-SIM ou 0-NÃO: \n"))

p_e = int(input("Já trabalhou com a vítima? 1-SIM ou 0-NÃO: \n"))

soma_p = p_a + p_b + p_c + p_d + p_e

if (soma_p < 2):
    print("\nInocente")
elif (soma_p == 2):
    print("\nSuspeito")
elif (soma_p <=4 and soma_p >=3):
    print("\nCúmplice")
elif (soma_p == 5):
    print("\nAssassino")
