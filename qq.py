a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите c: "))
if a<=b+c and b<=a+c and c<=a+b:
  print("Треугольник существует!")
if a==b and a==c and b==c:
  print("Треугольник равносторонний")
if a==b and a!=c:
  print("Треугольник равнобедренный")