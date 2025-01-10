def number():
    result=()
n=int(input('задайте любое число от 3 до 20: '))
for i in range(0,20):
    for j in range(1, i):
         if n % (i + j) == 0:
             result=i,j

             print(*result)
