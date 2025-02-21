# Упражнение 5: Сдаём бутылки
small_bottle_price = 0.10  # Цена за бутылку 1 литр и меньше
large_bottle_price = 0.25  # Цена за бутылку больше 1 литра

small_count = int(input("Введите количество бутылок 1 литр и меньше: "))
large_count = int(input("Введите количество бутылок больше 1 литра: "))

total = small_count * small_bottle_price + large_count * large_bottle_price

print(f"Вы можете выручить: ${total:.2f}")