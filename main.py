from bus import Bus
from train import Train
from plane import Plane
from docx import Document

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
        save = (input("Сохранить отчет (да/нет) "))
        if (save == "да" or save == "Да"):
            file = word(bus, "Автобус")
            print("Отчет сохранен")
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
def excel():
    print("")
"""сохранение в БД"""


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