# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
# в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for item in numbers:
    if item == 1:
        continue
    for j in range(2, item):    # Начало равно концу → нет ни одного числа, удовлетворяющего условию start ≤ j < stop
        if item % j == 0:
            not_prime.append(item)
            break
    else:
        prime.append(item)
print('Primes:', prime)
print('Not Primes:', not_prime)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
not_prime = []
for numb in numbers:
    if numb == 1:
        continue
    is_prime = True                 # используем логическую переменную
    for denom in range(2, numb):    # используем условие для определения чему эта переменная равна True / False
        if numb % denom == 0:
            is_prime = False
            break
    if not is_prime:                # в зависимости от переменной после проверки, если условие выполнилось - false
        not_prime.append(numb)      # добавляет число в not_prime
    else:                           # # если все было дробным, то есть условие не выполнено, переменная осталась True
        prime.append(numb)          # добавляет число в prime
print('Primes:', prime)
print('Not Primes:', not_prime)



