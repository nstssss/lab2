from bus import Bus
from train import Train
from plane import Plane
from docx import Document
from openpyxl import Workbook

""""""
def traveling_by_bus():
    print("Путешесвтие на автобусе: \n")
    try:
        distance = float(input("Введите расстоение маршрута в км: "))
        passengers = int(input("Введите количество пассажиров: "))
        price = float(input("Введите стоимость билета: "))

        if (distance >= 0 and passengers >= 0 and price >= 0):
            # создание экземпляра класса
            bus = Bus(distance, passengers, price)
            print(f"\nСтоимость маршрута: {bus.calculate_cost()} руб.")
            print(f"Время поездки: {bus.calculate_time()} часов" )
            print(f"Пассажиропоток: {bus.calculate_passenger_flow()}" )
        print("Сохранить?")
        save = input()
        if (save == "yes"):
            excel( bus, "Автобус")
    except(ValueError):
        print("Ошибка! Неверный ввод параметров")

""" """
def traveling_by_train():
    print("Путешествие на поезде: \n")
    try:
        distance = float(input("Введите расстоение маршрута в км: "))
        passengers = int(input("Введите количество пассажиров: "))
        price = float(input("Введите стоимость билета: "))

        if (distance >= 0 and passengers >= 0 and price >= 0):
            #создание экземпляра класса
            train = Train(distance, passengers, price)
            print(f"\nСтоимость маршрута: {train.calculate_cost()} руб.")
            print(f"Время поездки: {train.calculate_time()} часов")
            print(f"Пассажиропоток: {train.calculate_passenger_flow()}")

    except(ValueError):
        print("Ошибка! Неверный ввод параметров")
""" """
def traveling_by_plane():
    print("Путешествие на самолете: \n")
    try:
        distance = float(input("Введите расстоение маршрута в км: "))
        passengers = int(input("Введите количество пассажиров: "))
        price = float(input("Введите стоимость билета: "))

        if (distance >= 0 and passengers >= 0 and price >= 0):
            # создание экземпляра класса
            plane = Plane(distance, passengers, price)
            print(f"\nСтоимость маршрута: {plane.calculate_cost()} руб.")
            print(f"Время поездки: {plane.calculate_time()} часов")
            print(f"Пассажиропоток: {plane.calculate_passenger_flow()}")

    except(ValueError):
        print("Ошибка! Неверный ввод параметров")

"""Сохранение в  word"""
def word(transport_type, file_name):
    doc = Document()
    doc.title = f"Отчет <<Путешествие на {transport_type}>>"
    doc.add_heading("Характеристики маршрута", 2)
    doc.add_paragraph(f"Расстояние маршрута: {transport_type.distance} км")
    doc.add_paragraph(f"Количество пассажиров: {transport_type.passengers}  ")
    doc.add_paragraph(f"Стоимость билета: {transport_type.ticket_price} руб.")

    doc.add_paragraph()

    doc.add_heading("Расчеты: ", 2)

    doc.add_paragraph(f"Стоимость маршрута: {transport_type.distance} руб.")
    doc.add_paragraph(f"Время поездки: {transport_type.distance} час.")
    doc.add_paragraph(f"Пассажиропоток: {transport_type.distance} ")

    doc.save(f"{file_name}.docx")

"""Сохранение в excel"""
def excel(transport_type, file_name):
    wb = Workbook()
    ws = wb.active

    ws['A1'] = "Отчет <<Путешествие"
    ws['A3'] = "Характеристики маршрута"

    parameters = [
        ('Расстояние маршрута', f'{transport_type.distance} км'),
        ('Количество пассажиров', transport_type.passengers),
        ('Стоимость билета', f'{transport_type.ticket_price} руб.')
    ]
    for i, (param, value) in enumerate(parameters, 4):
        ws[f'A{i}'] = param
        ws[f'B{i}'] = value

    ws['A7'] = "Расчеты:"
    results = [
        ('Общая стоимость маршрута', f'{transport_type.calculate_cost()}'),
        ('Время поездки', f'{transport_type.calculate_time()}'),
        ('Пассажиропоток', f'{transport_type.calculate_passenger_flow()} ')
    ]
    for i, (result, value) in enumerate(results, 10):
        ws[f'A{i}'] = result
        ws[f'B{i}'] = value
    wb.save(f"{file_name}.xlsx")
    print("Отчет сохранен")

"""сохранение в БД"""

def choosing_to_save(transport_type, file_name):
    try:
        save = input("Сохранить отчет? (yes/no)")
        if (save == "yes" or save == "Yes"):
            print("\nВыберите формат отчета: ")
            print("1. Word")
            print("2. Excel")
            print("3. BD")
            print("4. Выйти")
            num = int(input())
            if (num < 1 or num > 4):
                print("Выберите действие от 1 до 4")
                if (num == "1"):
                    word(transport_type, file_name)
                elif(num == "2"):
                    excel(transport_type, file_name)
                else:
                    print("potom")
    except(ValueError):
        print("Ошибка! Неверный ввод")

def main():
    while(True):
        print("Выберите действие: \n")
        print("1. Путешествие на автобусе")
        print("2. Путешесвтие на поезде")
        print("3. Путешествие на самолете")
        print("4. Выход")

        try:
            choice = int(input("Ваш выбор: "))
            if (choice < 1 or choice > 4):
                print("Ошибка! Выберите действие (1-4)")
            if choice == 1:
                traveling_by_bus()
            elif choice == 2:
                traveling_by_train()
            elif choice == 3:
                print()
            elif choice == 4:
                break
        except(ValueError):
            print("Ошибка! Неверный ввод")

if __name__ == '__main__':
    main()