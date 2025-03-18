class SchoolManagementSystem:
    def __init__(self):
        self.classes = {"1A": [], "1B": [], "1C": [], "1D": []}  # Четыре первых класса

    def add_student(self, class_name: str, student_name: str):
        """Добавляет ученика в указанный класс"""
        if class_name in self.classes:
            self.classes[class_name].append(student_name)
            print(f"Ученик {student_name} добавлен в класс {class_name}.")
        else:
            print("Ошибка: указанного класса не существует.")

    def remove_student(self, class_name: str, student_name: str):
        """Удаляет ученика из указанного класса"""
        if class_name in self.classes and student_name in self.classes[class_name]:
            self.classes[class_name].remove(student_name)
            print(f"Ученик {student_name} удалён из класса {class_name}.")
        else:
            print("Ошибка: ученик не найден или указанного класса не существует.")

    def edit_student(self, class_name: str, old_name: str, new_name: str):
        """Редактирует имя ученика в указанном классе"""
        if class_name in self.classes and old_name in self.classes[class_name]:
            index = self.classes[class_name].index(old_name)
            self.classes[class_name][index] = new_name
            print(f"Ученик {old_name} теперь называется {new_name} в классе {class_name}.")
        else:
            print("Ошибка: ученик не найден или указанного класса не существует.")

    def display_students(self, class_name: str):
        """Выводит список учеников в указанном классе"""
        if class_name in self.classes:
            print(
                f"Ученики в классе {class_name}: {', '.join(self.classes[class_name]) if self.classes[class_name] else 'Нет учеников'}")
        else:
            print("Ошибка: указанного класса не существует.")


# Пример использования
school = SchoolManagementSystem()
school.add_student("1A", "Иванов Иван")
school.add_student("1B", "Петров Пётр")
school.display_students("1A")
school.edit_student("1A", "Иванов Иван", "Сидоров Алексей")
school.remove_student("1B", "Петров Пётр")
school.display_students("1B")
