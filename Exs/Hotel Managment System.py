class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # Словарь для хранения занятых номеров

    def add_client(self, room_number: int, client_name: str):
        """Добавляет клиента в гостиницу"""
        if room_number not in self.rooms:
            self.rooms[room_number] = client_name
            print(f"Клиент {client_name} заселён в номер {room_number}.")
        else:
            print("Ошибка: Номер уже занят.")
        self.show_occupied_rooms()

    def remove_client(self, identifier):
        """Удаляет клиента из гостиницы по номеру комнаты или имени клиента"""
        if isinstance(identifier, int):  # По номеру комнаты
            if identifier in self.rooms:
                del self.rooms[identifier]
                print(f"Номер {identifier} теперь свободен.")
            else:
                print("Ошибка: Номер не найден.")
        elif isinstance(identifier, str):  # По имени клиента
            for room, name in list(self.rooms.items()):
                if name == identifier:
                    del self.rooms[room]
                    print(f"Клиент {identifier} выселен из номера {room}.")
                    break
            else:
                print("Ошибка: Клиент не найден.")
        self.show_occupied_rooms()

    def show_occupied_rooms(self):
        """Выводит список занятых номеров"""
        if self.rooms:
            print("Занятые номера:", ", ".join(map(str, self.rooms.keys())))
        else:
            print("Все номера свободны.")


# Запуск программы
hotel = HotelManagementSystem()
while True:
    print("\nLesson 23 DA. Добавить клиента")
    print("2. Удалить клиента")
    print("Lesson 24 DA. Показать занятые номера")
    print("Lesson 25 DA. Выход")
    choice = input("Выберите действие: ")

    if choice == "Lesson 23 DA":
        room = int(input("Введите номер комнаты: "))
        name = input("Введите имя клиента: ")
        hotel.add_client(room, name)
    elif choice == "2":
        identifier = input("Введите номер комнаты или имя клиента: ")
        if identifier.isdigit():
            identifier = int(identifier)
        hotel.remove_client(identifier)
    elif choice == "Lesson 24 DA":
        hotel.show_occupied_rooms()
    elif choice == "Lesson 25 DA":
        print("Выход из программы.")
        break
    else:
        print("Ошибка: Некорректный выбор.")
