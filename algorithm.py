# на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
import random

def quicksort(array, left, right):
    p = random.choice(array)
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        quicksort(array, left, j)
    if right > i:
        quicksort(array, i, right)
    return array

# Поиск позиции элемента в последовательности
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle, right)

#Проверка правильности ввода
check = False

while not check:
    try:
        nums = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
        check = True
    except ValueError:
        print('Последовательность неверная. Попробуйте снова!')

sort_nums = quicksort(nums, 0, len(nums) - 1)
print(sort_nums)

second_check = False

while not second_check:
    try:
        x = int(input('Введите любое число: '))
        second_check = True
    except ValueError:
        print('Вы ввели не число. Попробуйте снова!')

if x > max(sort_nums) or x <= min(sort_nums):
    print("Элемент больше максимального либо меньше либо равен минимальному")
else:
    print("Индекс искомого элемента равен: ", binary_search(sort_nums, x, 0, len(nums)))