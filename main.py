# Задача №38.  Создать телефонный справочник с возможностью импорта
# и доработать метод search. Ваша программа не должна быть линейной
import functions as func


while True:
    print('1. вывод, 2. добавление, 3. поиск')
    mode = int(input())
    if mode == 1:
        func.show_data()
    elif mode == 2:
        func.add_data()
    elif mode == 3:
        func.find_data()
    elif mode == 4:
        func.search()

    else:
        break