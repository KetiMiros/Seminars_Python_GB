# напишите функцию, которая определит два соседних и, при этом
# оба соседних элемента меньше данного.

# <function_name> [ 1,3,3,5]> [5]
# <function_name> [ 1,5,1,6,1]> [5,6]

def fun1(number: list) -> list:                              #показываем, что будет на выходе(list)
    result = []
    for ind, element in enumerate(number):
        prev_ind = ind - 1
        next_ind = ind + 1 if ind != len(number) - 1 else 0
        if number[prev_ind] < element and number[next_ind] < element:
            result.append(element)
    return result

user_lst = [8, 1, 5, 4, 5]
print(fun1(user_lst))