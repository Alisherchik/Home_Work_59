#Упражнение 7: Сумма первых n положительных чисел

# Запрашиваем у пользователя число n
n = int(input("Введите число n: "))

# Вычисляем сумму первых n натуральных чисел по формуле
sum_n = (n * (n + 1)) // 2  # Используем целочисленное деление для целого результата

# Выводим итоговую сумму
print(f"Сумма первых {n} положительных чисел: {sum_n}")