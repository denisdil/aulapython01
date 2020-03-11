print("calculo de maior")
a=float(input("entre com a primeiro valor: "))
b=float(input("entre com a segundo valor: "))
c=float(input("entre com a terceiro valor: "))

if a>b or a>=c:
   print("%d"%a)
elif a==b and b==c :
    print("Triangulo é equilatero")
elif a==b or b==c or c==a :
    print("Triangulo é isosceles")
else:
    print("Triangulo é escaleno")
