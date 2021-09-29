import operator
import os
# Найдите три ключа с самыми высокими значениями в словаре
dict = {'1key': 123, '2key': 9785, '3key': 560, '4key': 234, '5key': 3451}

dict_s = list(sorted(dict.items(), key=operator.itemgetter(1)))
dict_s = [dict_s.pop() for _ in (range(len(dict_s) - (3 - 1)))]
dict = {k: v for k, v in dict_s}
print(dict)

#Находит строке числа и добавляет их
a = 'as1sd3asd44asd asa sd 5 asd 43'
b = 'as123sdasdasd asa sd 5 asdasd 42 234'
# фильтр несовсем то, так как выносит все по одному символу и числа разбивает на отдельные цыфры,
# потом возни много
def sep(value):
    for i in value:
        if i.isnumeric() == False:
           value = value.replace(i, " ")
    value = value.split()
    b = sum([int(i) for i in value])
    return print(b)
sep(a)
sep(b)

#Раздница двух массивов (Уникальные значения)
a = ([1, 3, 4], [2, 4, 5])
b = ([1, 2, 3], [2, 4, 5])
#print(len(a))
#print(a[0][2])
# можно было сделать несколько проще c доступом через индексы,  было меньше кода но в данном случае
#присутсвует динамика и теоритически можно развить функцию (полсе доработки) для многомерных масивов
def mas(value):
    for i in range(len(value) - 1):
        a_1 = list((set(value[i]).difference(set(value[i + 1]))))
        a_2 = list((set(value[i + 1]).difference(set(value[i]))))
    print(f'Двумерный масив имеет уникальные значения - в первом списке {a_1}, во втором списке {a_2}.')
mas(a)
mas(b)

# f_n = 3
# Func(5,  f_n) -> n + nn + nnn = 615
# n = 5
# f_n = 4
# Func(5,  f_n) -> n + nn + nnn + nnnn = 6170
#исхдя из структуры задачи наиболее с точки зрения кода интересным будет решение через рекурсию,
#но все источники не рекомендуют такое решение как неоптимальное с точьки зрения расхода памяти, поэтому
# реализовано через универсальный цыкл
def task(n, x=5):
    f = [x]
    if n == 1:
        return print(x)
    for i in (range(2, n + 1)):
        f.append(x + (f[i - 2] * 10))
    return print(sum(f))
task(1)
task(3)
task(4)
task(4,8)
#Факториал числа + кеш

# Всё работает но есть поблема, хранить кеш надо во глобальной переменной, иначе несохраняется
# после работы функции, это не есть хорошо с точьки зрения дизайна, есть в сети упоминания о возврате дангных
# функции снова в функцию через аргумент, но толкового описания или примера не нашел возможно байка
# в принципе наиболее оптимальное решение обернуть в класс, но задача стаяла сделать функцией

w = {}
def factorial(walue):
    factorial = 1
    if w.setdefault(walue) != None:
        factorial = w.setdefault(walue)
    else:
        for i in range(2, walue + 1):
            factorial *= i
            w[walue] = factorial
    return print(walue, 'factorial', factorial, '\n', w)

factorial(2)
factorial(3)
factorial(4)
factorial(5)
factorial(6)
factorial(3)

#Выведите список файлов в указанной директории.

for x in os.listdir('.'):
     print(x)
