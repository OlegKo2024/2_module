print('This is a webinar on 30.06.2024')
"""
year = int(input('Enter year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('V')
else:
    print('N')

year = int(input('Enter year: '))
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print('V')
else:
    print('N')
"""
print('КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ - WHILE')
print('method_1')
# number = int(input('Enter a number: '))
# l = 0
# while number > 0:
#     l += 1
#     number = number // 10
# print(l)
# идет замена введенного числа новым целым числом, которое получает делением на 10, то есть мы откусываем постепенно
# крайне правое число и когда мы приходим к 1 // 10, условие > 0 не выполняется и мы получаем количество итераций.
# что и является длиной числа

# print('method_2')
# number = int(input('Enter a number: '))
# number = str(number)
# print(type(number))
# print(len(number))
# для строки чисел len не считается

# l = [1, 'я', 3, 4]
# print(len(l))

print('СУММА ЦИФР В ЧИСЛЕ - WHILE')
number = int(input('Enter a number: '))
s = 0
while number > 0:
    s += number % 10              # здесь происходит суммирование откусываемых цифр: 0+6, +
    number = number // 10         # здесь происходит замещение предыдущего значения получаемым значением после откусывания
print(s)

print('ЦИФРЫ МЕЖДУ ЧИСЛАМИ - WHILE')
a = int(input('Enter first number '))       # 13
b = int(input('Enter second number '))      # 18
i = a + 1                 # переменная счетчик, начал с 11 - ok
while i < b:              # 11 < 15 - да, идем дальше
    print(i, end=' ')     # печать первого символа - 11
    i += 1                # замещаем i на 12 и т.д.
#                         # получили цифры между 11 12 13 14 (вводили 10 и 15)

print('ЦИФРЫ МЕЖДУ ЧИСЛАМИ - FOR')
# a = int(input('Enter first number '))
# b = int(input('Enter second number '))
# for i in range(a+1, b):
#     print(i, end=' ')
# получили цифры между 11 12 13 14 (вводили 10 и 15)

# print('СПИСКИ - FOR')
# l = ['z', 1, 1.1]
# for i in l:
#     print(i, end=' ') # получили z 1 1.1

print('СПИСКИ - FOR - ЗАМЕНА')

l = [7, 8, 9, 11, 13]
for i in range(len(l)):
    l[i] *= 2
    print(l, end=' ')
# получили [14, 8, 9, 11, 13] [14, 16, 9, 11, 13] [14, 16, 18, 11, 13] [14, 16, 18, 22, 13] [14, 16, 18, 22, 26]

l = [7, 8, 9, 11, 13]
for i in range(len(l)):
    l[i] *= 2
print(l, end=' ')
# получили [14, 16, 18, 22, 26]

l = [3, 4, 5, 6, 7]
for i in range(len(l)):   # последовательность здесь от 0 до 4, 5 не включается и далее ...
    l[i] **= l[i]         # первый член [0]=3 в степени себя 3 = 3*3*3 =27 и так далее, получаем в степени значения данного числа.
print(l, end=' ')
# Получили [27, 256, 3125, 46656, 823543]

l = [3, 4, 5, 6, 7]
for i in range(len(l)):  # последовательность здесь от 0 до 4, 5 не включается и далее ...
    l[i] *= l[i]         # первый член [0]=3 * себя 3 и так далее, получаем перемножение самого на себя
print(l, end=' ')
# [9, 16, 25, 36, 49] если в квадрате l[i] *= l[i]

l = [3, 4, 5, 6, 7]
for i in range(len(l)):     # последовательность здесь от 0 до 4, 5 не включается и далее ...
    l[i] **= 2              # первый член [0]=3 в степени 2 и так далее, получаем каждое число в степени 2
print(l, end=' ')
# [9, 16, 25, 36, 49]

# for перебирает весь список или строку, но если range, то от начального (если нет то 0) до указанного значений, его не включая.

l = [3, 4, 5, 6, 7]
for i in l:
    i = i * i
print(l)       # [3, 4, 5, 6, 7] не можем заменить, элементы списка, так как i указывает на другое число


l = [3, 4, 5, 6, 7]
for i in l:
    i *= i
    print(i, end=' ')       # 9 16 25 36 49

l = [3, 4, 5, 6, 7]
l = [i * i for i in l]
print(l)                    # [9, 16, 25, 36, 49] но можно так


for i in range(1970, 2025):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i, end=' ')

l = []
def black_years(y_start, y_end):
    for i in range(y_start, y_end):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            l.append(i)
    print(l)

black_years(2024, 2030)
