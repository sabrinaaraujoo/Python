import math

#ENTADAS
a = int(input("Digite o valor da var a: "))
b = int(input("Digite o valor da var b: "))
x = int(input("Digite o valor da var x: "))

#PROCESSAMENTO
y = (math.pow(a,2) + math.sqrt(3*b))/(5*math.pow(x,3))

x = y + math.sqrt((2*b)/(a+b))

#SAIDA
print("a) y = ",y)
print("a) x = ",x)
