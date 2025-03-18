# Получаем первое число от пользователя
num1 = float(input("Введите первое число: "))

# Получаем математический оператор (+, -, *, /)
operator = input("Введите оператор (+, -, *, /): ")

# Получаем второе число от пользователя
num2 = float(input("Введите второе число: "))

# Проверяем оператор и выполняем соответствующую операцию
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль"
else:
    result = "Ошибка: некорректный оператор"

# Выводим результат
print("Результат:", result)