from collections import deque

# Определение структуры данных для квартиры
class Apartment:
    def __init__(self, street, house_number, apartment_number):
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number

# Создание стека
stack = deque()

# Функция для добавления квартиры в стек
def add_apartment(stack, street, house_number, apartment_number):
    apartment = Apartment(street, house_number, apartment_number)
    stack.append(apartment)

# Функция для просмотра данных стека и подсчета домов на улице "Дерибасовская"
def count_houses_on_deribasovskaya(stack):
    count = 0
    for apartment in stack:
        if apartment.street == "Дерибасовская":
            count += 1
    return count

# Пример добавления квартир в стек
add_apartment(stack, "Дерибасовская", 10, 5)
add_apartment(stack, "Пушкинская", 20, 10)
add_apartment(stack, "Дерибасовская", 15, 7)

# Добавление новой квартиры
add_apartment(stack, "Дерибасовская", 25, 12)

# Просмотр данных стека
print("Данные стека:")
for apartment in stack:
    print(f"Улица: {apartment.street}, Номер дома: {apartment.house_number}, Номер квартиры: {apartment.apartment_number}")

# Подсчет количества домов на улице "Дерибасовская"
count_deribasovskaya = count_houses_on_deribasovskaya(stack)
print(f"Количество домов на улице 'Дерибасовская': {count_deribasovskaya}")
