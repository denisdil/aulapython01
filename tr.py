print("calculo de um triangulo")
a=float(input("entre com a primeira medida: "))
b=float(input("entre com a segunda medida: "))
c=float(input("entre com a terceira medida: "))

if a>=b+c or b>=c+a or c>=a+b :
   print("Triangulo inexistente.")
elif a==b and b==c :
    print("Triangulo é equilatero")
elif a==b or b==c or c==a :
    print("Triangulo é isosceles")
else:
    print("Triangulo é escaleno")
