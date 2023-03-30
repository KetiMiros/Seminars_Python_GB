# # даны два списка. Требуется вывести те элементы,
# первого массива, которых нет во втором. 
# Пользователь вводит
# число N- количестов эл. в первом массиве, затем N-
# # чисел - элементы массива.

# lst1 =[(input(" Введите число элементов в массиве: "))]
# импротируем счетчик 

from time import perf_counter # импротируем счетчик 
# from random import randint 

          
lst1 = [1,25,6,5,7,2,2,15,15]
lst2 = [1,45,6,5,25,78,9]

def fun(lst1, lst2):
    # lst_all = set(lst1).difference(set(lst2))
    t1 = perf_counter()
    rez = list(set(lst1).difference(set(lst2)))
    t2 = perf_counter()
    return rez, t2-t1

print(fun(lst1, lst2))

# ----------------------второй вариант решения----------------

def fun2(lst1,lst2):
    t1 = perf_counter()
    lst_a = []
    for i in lst1:
        if i not in lst2:
            lst_a.append(i)
    t2 = perf_counter()
    return lst_a, t2 - t1
   

print(fun2(lst1,lst2))

