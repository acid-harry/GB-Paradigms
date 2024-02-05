def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Нашли элемент, возвращаем его индекс
        elif mid_element < target:
            left = mid + 1  # Искомый элемент находится справа от центрального
        else:
            right = mid - 1  # Искомый элемент находится слева от центрального

    return -1  # Элемент не найден

# Ввод массива и целевого элемента через консоль
arr = list(map(int, input("Введите отсортированный массив чисел через пробел: ").split()))
target_element = int(input("Введите целевой элемент для поиска: "))

# Вызов функции бинарного поиска и вывод результата
result = binary_search(arr, target_element)
if result != -1:
    print(f"Элемент {target_element} найден по индексу {result}.")
else:
    print(f"Элемент {target_element} не найден в массиве.")