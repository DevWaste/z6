def min_boats(weights, m):
    weights.sort()
    i, j = 0, len(weights) - 1
    boats = 0

    while i <= j:
        # Если вес двух рыбаков меньше или равен максимальному допустимому весу
        if weights[i] + weights[j] <= m:
            i += 1  # берем легчайшего
        j -= 1  # всегда берем тяжелейшего
        boats += 1  # одна лодка либо с двумя, либо с одним рыбаком

    return boats

# Ввод данных
m = int(input("Введите максимальную массу, которую может выдержать одна лодка: "))
n = int(input("Введите количество рыбаков: "))
weights = [int(input("Введите вес рыбака: ")) for _ in range(n)]

# Вывод результата
print("Минимальное количество лодок:", min_boats(weights, m))
