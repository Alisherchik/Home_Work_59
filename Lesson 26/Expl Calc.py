def calculate_percentage(total: float, percent: float) -> float:
    """
    Вычисляет определённый процент от числа.

    :param total: Целое число, от которого вычисляется процент.
    :param percent: Значение процента.
    :return: Результат вычисления.
    """
    return (total * percent) / 100


# Пример использования
result = calculate_percentage(200, 15)  # 15% от 200
print(result)  # Выведет 30.0
