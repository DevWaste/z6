# Ввод количества чисел
N = int(input("Введите количество чисел: "))

# Ввод чисел и добавление их в список
numbers = []
for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

# Переворачиваем массив
reversed_numbers = numbers[::-1]

# Вывод перевернутого массива
print(" ".join(map(str, reversed_numbers)))
