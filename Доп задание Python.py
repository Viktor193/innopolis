#1. Напишите программу, которая найдет все такие числа, которые делятся на 7, но не #делятся на 5, от 2000 до 3200 (включая оба). Полученные числа должны быть напечатаны в #последовательности, разделенной запятыми, в одной строке.

k=2000
while k<=3200:
  if k/7==int(k/7) and k/5!=int(k/5):
    print(k,', ', end='')
    k+=1
  else:
    k+=1  


#2. Напишите программу, которая может вычислить факториалы заданных чисел. Результаты должны быть напечатаны в последовательности, разделенной запятыми, в одной строке.

print ('\n введите количевство чисел ', end='')
n=input()
array_1=[]
for _ in range(int(n)):
  print ('введите',_,'число: ', end='')
  array_1+=list(map(int, input().split()))

for _ in range(int(n)):
  
  f=1
  if array_1[_]>0:
    for i in range(2,array_1[_]+1):
      f*=i
    print(f, ', ',end='')
  else:
    print ('не натуральное число:', array_1[_],', ',end='')



#3. Напишите программу, которая принимает 2 числа X, Y в качестве входных данных с клавиатуры и генерирует двумерный массив. Значение элемента в i-й строке и j-м столбце массива должно быть i*j.  (нумерация с нуля)

print ('\n введите m ', end='')
m=int(input())
print ('\n введите n ', end='')
n=int(input())
array_1 = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
  for j in range (n):
    array_1[i][j] = j * i
print(*array_1, sep='\n')

#4. Веб-сайт требует, чтобы пользователи вводили имя пользователя и пароль для регистрации. Напишите программу для проверки правильности ввода пароля пользователями.

import re
print('Введите пароль: ',end='')
p = input()
if len(p) > 12:
  print('Максимальная длина пароля транзакции: 12')
elif len(p) < 6:
  print('Минимальная длина пароля транзакции: 6')  
elif not re.search("[0-9]", p):
  print('Пароль должен содержать хотя бы 1 число между [0–9]')
elif not re.search("[a-z]", p):
  print('Пароль должен содержать минимум 1 буква между [a-z]')
elif not re.search("[A-Z]", p):
  print('Пароль должен содержать хотя бы 1 буква между [A–Z]')
elif not re.search("[$#@]", p):
  print('Пароль должен содержать хотя бы 1 символ из [$#@]')  
else:
  print('Успешно создан пароль')
