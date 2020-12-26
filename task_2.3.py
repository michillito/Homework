seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Январь',
                2: 'Февраль',
                3: 'Март',
                4: 'Апрель',
                5: 'Май',
                6: 'Июнь',
                7: 'Июль',
                8: 'Август',
                9: 'Сентябрь',
                10:'Октябрь',
                11:'Ноябрь',
                12:'Декабрь'}
month = int(input("Введите месяц по номеру: "))
if month == 12:
        print(seasons_dict.get(12))
        print(seasons_list[0])
elif month == 1:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 2:
        print(seasons_dict.get(2))
        print(seasons_list[0])

elif month == 3:
    print(seasons_dict.get(3))
    print(seasons_list[1])
elif month == 4:
    print(seasons_dict.get(4))
    print(seasons_list[1])
elif month == 5:
    print(seasons_dict.get(5))
    print(seasons_list[1])

elif month == 6:
    print(seasons_dict.get(6))
    print(seasons_list[2])
elif month == 7:
    print(seasons_dict.get(7))
    print(seasons_list[2])
elif month == 8:
    print(seasons_dict.get(8))
    print(seasons_list[2])

elif month == 9:
    print(seasons_dict.get(9))
    print(seasons_list[3])
elif month == 10:
    print(seasons_dict.get(10))
    print(seasons_list[3])
elif month == 11:
    print(seasons_dict.get(11))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")