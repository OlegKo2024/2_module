def rect(h, w):
    for i in range(h):
        print('*' * w)

rect(3, 5)
print(rect)


print('ЦИКЛ WHILE')

l = [4, 5, 6]
i = 0
while i < len(l):
    print(l[i])             # 4 5 6
    i += 1

print('ПРОПУСТИТЬ 6')
l = [2, 3, 5, 6, 10]
i = 0
while i < len(l):
    if l[i] == 6:
        i += 1
        continue
    print(l[i], end=' ')
    i += 1

n = 5
arr = []
for i in range(n):
    arr.append([])
print(arr)


n = 3
m = 4
l = 10
arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append(l)
print(arr)                  # [[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]]


print('ЗАКОНЧИТЬ ЦИКЛ НА 10')

l = [2, 3, 5, 6, 10]
i = 0
while i < len(l):
    if l[i] == 10:
        print('попал на 10')
        break
    print(l[i], end=" ")
    i += 1

print('ЦИКЛ FOR')
l = 'Hi there'                 # принимает значения элементов строки
for i in l:
    print(i, end='')           # Hi there

l = [2, 'Hi', 5, 'Hello', 10]
for i in l:
    print(i, end=' ')           # принимает значения списка

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True         # должны использовать лог/ переменную, в завис. чему = эта перем. мы добавляет число в prime или not_prime
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
    else:
        not_prime.append(i)
print('Primes:', prime)
print('Not Primes:', not_prime)

print('ИСПОЛЬЗУЯ ЛОГИЧЕСКИЕ ЗНАЧЕНИЯ В ФУНКЦИЯХ')
def contains(string, list_to_search):
    is_in = []
    is_not = []
    string = string.upper()
    list_to_search = [i.upper() for i in list_to_search]
    print(string)
    print(list_to_search)
    for i in list_to_search:
        it_contains = True
        if i not in string:
            it_contains = False
        if it_contains:
            print('I am in')
            is_in.append(i)
            print(is_in)
        else:
            print('I am NOT in')
            is_not.append(i)
            print(is_not)
    print(is_in)
    print(is_not)

contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
contains('cycle', ['recycling', 'cyclic']) # No matches
contains('Disablement', ['Able', 'Mable', 'Disable', 'Bagel'])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            not_prime.append(i)
            break
    else:
        prime.append(i)
print('Primes:', prime)
print('Not Primes:', not_prime)

def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))


print('FUNCTIONS')
def xhi(name, age):
    print('Hi', name)
    print('You are', age)


xhi('Oleg', 57)

def xhi(name, age):
    print(f'Hi, {name}')
    print(f'You are {age}')


xhi('Tania', 55)

def xhi(name, age):
    return (f'Hi, {name}\
            You are {age}')


z = xhi('Nikita', 19)
print(z)

