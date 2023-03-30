#  Дан список чисел. посчитайте, скоько в нем пар элементов равных друг дургу
# Если два элемент равны, то образуют пару, которую нужно посчитать

# Пример:
#       <function> ([1, 2, 3, 2, 3]) -> 2
#       <function> ([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

lst1 = [1, 2, 3, 2, 3, 3, 2, 4]
def user_lst(lst1):
    # lst2 = []
    count = 0
    for ind in range(len(lst1)):
        el  = lst1[ind]
        for ind_2 in range(ind + 1, len(lst1)):
            if el == lst1[ind_2]:
                count += 1
    return count

print(user_lst(lst1))

