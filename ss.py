for i in 1,3,5:
  print(i**5,sep="\n")
a = [5, 7, 17, 34]
for i in a:
  print(f'{i}**3={i**3}')
a=[5,7]
b=[5,3]
c=a+b
print(c)
for i in range(1,11,1):
  print(i)
a=str("Good")
print(a[0])
print(a[-1])
for i in range(0,10,1):
  if i<len(a):
    print(a[i]+'-Bad')
  else: print(f'{i} - Good')
x=int(input("Введите начальный вклад "))
y=int(input("Введите процент "))/100
n=int(input("Введите число лет "))
for i in range(0,n):
  x+=x*y
  print(x) #оформить вклад

for i in 'Hello world':
  if i=='o':
    break
  print(i)
for i in 'hello world':
  if i =='o':
    print(i)