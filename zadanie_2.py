def rearrange_array(arr):
    # Создаем новый пустой список для хранения результатов
    new_arr = [0] * len(arr)
    # Перемещаем последний элемент в начало нового списка
    new_arr[0] = arr[-1]
    # Добавляем оставшиеся элементы
    for i in range(1, len(arr)):
        new_arr[i] = arr[i - 1]
    return new_arr

# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

# Проверяем, что количество введенных чисел соответствует N
if len(arr) != N:
    print("Количество введенных чисел не соответствует заявленному. Пожалуйста, введите ровно", N, "чисел.")
else:
    # Обработка и вывод результата, если все в порядке
    result = rearrange_array(arr)
    print("Измененный массив:", result)
