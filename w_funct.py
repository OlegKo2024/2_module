import math


def distance(x1, y1, z1, x2, y2, z2):
    z = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return z
print(distance(0,0,0,1,1,0))

print('ПРИМЕР ФУНКЦИИ БЕЗ АРГУМЕНТОВ КОТОРАЯ НИЧЕГО НЕ ВОЗВРАЩАЕТ')
def hi():
    print('Hi')

hi()                  # Hi

print('ПРИМЕР ФУНКЦИИ С АРГУМЕНТАМИ КОТОРАЯ НИЧЕГО НЕ ВОЗВРАЩАЕТ')
def xhi(n):
    print('Hi ' * n)

xhi(5)                      # HiHiHiHiHi

print('ПРИМЕР ФУНКЦИИ С АРГУМЕНТАМИ КОТОРАЯ ВОЗВРАЩАЕТ РЕЗУЛЬТАТ')
def sum_sqrt_n(x1, x2):
    z = x1 + x2
    return z ** 2

print(sum_sqrt_n(2, 3)) # 25
# Что нам надо вернуть записывается после return


print('Et cetera - etc.')
def f(n):
    for i in range(n):
        if i > 5:
            return
            print(i, end=' ')

f(1)            # 0
f(2)            # 0 1
f(5)            # 0 1 2 3 4
f(6)            # 0 1 2 3 4 5
f(7)            # 0 1 2 3 4 5

print('sum_digits - преобразование строки в список чисел')
def sum_digits(n):
    list_ = ([int(d) for d in str(n)])
    print(list_)

sum_digits(1234)                    # [1, 2, 3, 4] преобразовали строку в список чисел

print('sum_digits - суммирование строки чисел через преобразование в список чисел а затем суммирование функцией')

def sum_digits(n):
    list_ = ([int(d) for d in str(n)])
    return sum(list_)

print(sum_digits(1234))             # 10 суммировали числа в строке

# number = input('Enter a number: ')
# c = sum_digits(number) * 2
# print(c)                          # 20 суммировали числа в строке

print('return завершает работы всей функции, если например, после return в функции что-то было, то оно не будет выполняться')
print('break же завершить работу цикла и если цикл в формуле и есть продолжение, то после break продолжение следует')
print('')

print('ФУНКЦИИ МОЖНО НЕ ТОЛЬКО ВЫЗЫВАТЬ, НО И ПЕРЕДАВАТЬ ИХ В ДРУГИЕ ФУНКЦИИ')

def key(student):
    return sum(student['mark']) / len(student['mark'])

number = int(input('Циклов: '))           # кол-во циклов
students = []                   # будущий список
for i in range(number):         # цикл, стоит _ так как не нужно имя переменной, но можно поставить и i
    line_ = input()             # Nikita 2004 3 4 4 5
    arr = line_.split()
    print(arr)                  # ['Nikita', '2004', '3', '4', '4', '5'] после print
    student = dict()            # создали словарь или можно student = {}
    print(student)
    student['name'] = arr[0]
    student['year'] = int(arr[1])
    student['mark'] = [int(m) for m in arr[2:]] # список значений m начиная с 3го и до конца
    students.append(student)
print(students)              # [{'Name': 'Nikita', 'Year': 2004, 'Mark': [3, 3, 3, 3]}, {'Name': 'Tim', 'Year': 2003, 'Mark': [4, 4, 4, 4]}]
students = sorted(students, key=key, reverse=True) # reverse=True сортировка от большего к меньшему
print(students)             # [{'Name': 'Tim', 'Year': 2003, 'Mark': [4, 4, 4, 4]}, {'Name': 'Nikita', 'Year': 2004, 'Mark': [3, 3, 3, 3]}]

