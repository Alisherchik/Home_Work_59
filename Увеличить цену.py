# milk = 100
# bread = 50
# chees = 200
#
# milk *= 1.1
# bread *= 1.1
# chees *= 1.1
#
# print("Новые цены:")
# print(f"Молоко: {milk}")
# print(f"Хлеб: {bread}")
# print(f"Сыр: {chees}")



# prices = {
#     "молоко": 100,
#     "хлеб": 50,
#     "сыр": 200
# }
#
# for product in prices.keys():
#     prices[product] *= 1.1
#     # prices[product] = round(prices[product] * 1.1)
# print(prices)




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def increase_price(self, percentage):
        self.price *= 1 + percentage / 100

# Список товаров
products = [
    Product("молоко", 100),
    Product("хлеб", 50),
    Product("сыр", 200)
]

# Увеличение цены каждого товара на 10%
for product in products:
    product.increase_price(10)

# Вывод новых цен
print("Новые цены:")
for product in products:
    print(f"{product.name}: {product.price}")
