#Упражнение 8: Сувениры и безделушки
# Определяем вес сувенира и безделушки в граммах
souvenir_weight = 75  # Вес одного сувенира
trinket_weight = 112  # Вес одной безделушки

# Запрашиваем у пользователя количество покупок каждого типа
souvenir_count = int(input("Введите количество сувениров: "))
trinket_count = int(input("Введите количество безделушек: "))

# Вычисляем общий вес посылки
total_weight = (souvenir_count * souvenir_weight) + (trinket_count * trinket_weight)

# Выводим итоговый вес
print(f"Общий вес посылки: {total_weight} гр.")