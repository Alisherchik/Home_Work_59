# Упражнение 5: Сдаём бутылки
small_bottle_price = 0.10  # Цена за бутылку Lesson 23 DA литр и меньше
large_bottle_price = 0.25  # Цена за бутылку больше Lesson 23 DA литра

small_count = int(input("Введите количество бутылок Lesson 23 DA литр и меньше: "))
large_count = int(input("Введите количество бутылок больше Lesson 23 DA литра: "))

total = small_count * small_bottle_price + large_count * large_bottle_price

print(f"Вы можете выручить: ${total:.2f}")


print('манго', 'апельсин', 'бананчик')