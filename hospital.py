#hospital

#entrada

ndias = int(input("Digite os dias no hospital: \n"))

tpquarto = input("Digite p-particular, s-semi-partucular, c-coletivo: \n")

if (tpquarto == "p"):
    diaria = ndias * 360
elif (tpquarto == "s"):
    diaria = ndias * 210
elif (tpquarto == "c"):
    diaria = ndias * 185
else:
    print("Digite apenas p/s/c para tipo de quarto neste hospital.")
    diaria = 0

wifi = input("Digite s-sim ou n-não para WI-FI:")

tv = input("Digite s-sim ou n-não para TV:")

if (wifi == "s"):
    resp_wifi = 3
else:
    resp_wifi = 0
    print("Digite apenas s/n")
    
if (tv == "s"):
    resp_tv = 4
else:
    resp_tv = 0
    print("Digite apenas s/n")

    total = diaria+resp_wifi+resp_tv

print("\n\n Hospital Comunitário:")
print("Número de dias no hospital: ",ndias)
print("Tipo de quarto: ",tpquarto)
print("Diarias:........ ",diaria)
print("Wi-fi:.......... ",resp_wifi)
print("TV a cabo:...... ",resp_wifi)
print("Total:.......... ",total)
