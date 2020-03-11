print("Entre com valores para executar um equação de 2 grau") 
a = int(input("Digite valor de a="))
b = int(input("Digite valor de b="))
c = int(input("Digite valor de c="))
delta = b**2 -4*a*c
if delta<0:
    print("equação inexistente")
else:
    print("delta = %d" %delta)
    x1= (-b+delta**(1/2))/(2*a)
    x2= (-b-delta**(1/2))/(2*a)
    print("x1= %d" %x1)
    print("x2= %d" %x2)