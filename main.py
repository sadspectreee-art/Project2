slovar = {
    'Миша': {'Оценки': [6, 8, 2, 3, 5]},
    'Айдан': {'Оценки': [9, 7, 4, 10]}}

try:
    def add_student():
        stud = input('Введите имя студента: ').title()
        if stud == '':
            print(f'Не оставляйте поле пустым!')
            menu()
            return
        print(f'Студент добавлен!')
        slovar[stud] = {'Оценки': []}
        print(slovar)
        x = input('Вернуться к меню?[1] / Добавить еще студента?[2] ')
        if x=='1':
            menu()
        elif x=='':
            print(f'Ошибка!')
        elif x=='2':
            add_student()
except ValueError:
    print(f"Ввели не символ!")
    menu()


def show_student():
    print(f"\f \f \f \f \f \f \f     Студенты: ")
    for name, info in slovar.items():
        print(f'Имя: {name} Оценки {info}')
    x = input('Вернуться к меню?[1] ')
    if x == '1':
        menu()
    elif x == '':
        print(f'Ошибка!')



def find_student():
    print(f'        Поиск студента')
    stu = input('Введите имя студента: ').title()
    if stu == '':
            print(f'Нельзя оставлять поле пустым!' )
            menu()
            return
    if stu in slovar:
        grades = slovar[stu]['Оценки']
        print(f'Студент найден {stu} Оценки: {grades} ')
    else:
        print(f'Студент не найден')
    x = input('Вернуться к меню?[1] / Поискать студента?[2] ')
    if x == '1':
        menu()
    elif x == '':
        print(f'Ошибка!')
    elif x == '2':
        find_student()



def change_rating():
    vibor = input('Для изменении оценки \nВведите имя студента: ').capitalize()
    if vibor == '':
        print(f'Нельзя оставить поле пустым!')
        menu()
        return
    for i in slovar:
        if vibor ==i:
            osen = input('Добавить(1) или удалить оценку?(2): ')
        if osen == '1':
            osen2 = int(input('Введите оценку: '))
            slovar[i]['Оценки'].append(osen2)
            print(f'Оценка добавлена!')
            print(slovar [i])
            return
        elif osen == '2':
            print(slovar[i]['Оценки'])
            osen3 = int(input('Какую оценку удалить?'))
            slovar[i]['Оценки'].remove(osen3)
            print('\f \f \f      Оценка удалена!')
            print(slovar[i])
            return
        else:
            print('Повторите заново!')
        x = input('Вернуться к меню?[1] / Изменить оценку студента[2] ')
        if x == '1':
            menu()
        elif x == '':
            print(f'Ошибка!')
        elif x == '2':
            change_rating()





def delete_student():
    vir = input('Введите имя студента: ').capitalize()
    if vir == '':
        print(f'Нельзя оставить поле пустым!')
        return
    for i in list(slovar): #создали лист так как во время удаления фор его читает
        if vir == i:
            del slovar[i]
            print(f'Студент успешно удален')
            print(slovar)
        x = input('Вернуться к меню?[1] / Удалить студента[2] ')
        if x == '1':
            menu()
        elif x == '':
            print(f'Ошибка!')
        elif x=='2':
            delete_student()


def sredball(): #В том числе автоматически использую везде i так как это локальное значение
    for i in slovar:
        osen = slovar[i]['Оценки']
        kol = len(osen)
        summa = sum(osen)
        sres = summa / kol
        print(slovar[i])
        print(f'Средний балл равен {sres}')
    x = input('Вернуться к меню?[1] ')
    if x == '1':
        menu()
    elif x == '':
        print(f'Ошибка!')


def exed():
    print(f'Выход из программы выполнен')
    menu()

def menu():
    print(f"""
-----------Меню программы------------
        1. Добавить студента
        2. Показать всех студентов
        3. Найти студента
        4. Изменить оценку
        5. Удалить студента
        6. Средний балл
        0. Выход""")
    try:
        choice = int(input("Введите число от 1 до 6: "))
    except ValueError:
        print(f"Ввели не число!")
        menu()
        return


    if choice == 1:
        add_student()

    elif choice == 2:
        show_student()
    elif choice == 3:
        find_student()
    elif choice == 4:
        change_rating()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        sredball()
    elif choice == 0:
        exed()
    elif choice == '':
        print('Нельзя оставлять пустым!')


menu()
