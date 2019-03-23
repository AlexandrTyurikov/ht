import json

# data_log = {'zx': '12'}
list_p = {}


# log_passw = {}


# with open('test3.json', 'w') as json_file:
#    json.dump(data_log, json_file)

def reg():
    log1 = input('Придумайте и введите логин: ')
    passw1 = input('Придумайте и введите пароль: ')
    with open('data_log.txt', 'r') as json_file_read:
        data_log = json.load(json_file_read)
    # print(data_log)
    if log1 in data_log.keys():
        print('Такой логин существует. Введите новый.')
        return reg()
    data_log[log1] = passw1
    with open('data_log.txt', 'w') as json_file_w:
        json.dump(data_log, json_file_w)
    print('Вы зарегистрировались. Войдте в систему:')
    vhod_v_sis()


def vhod_v_sis():
    log2 = input('Введите логин: ')
    passw2 = input('Введите пароль: ')
    with open('data_log.txt', 'r') as json_file_read:
        data_log = dict(json.load(json_file_read))
    if log2 not in data_log.keys():
        print('Такого логина не существует.Введите другой или зарегестрируйтесь!')
        return vhod()
    if passw2 != data_log[log2]:
        print('Пороль не совпадает. Повтоите попытку')
        return vhod_v_sis()
    else:
        menu()


def vhod():
    print('Добро пожаловать в ИМТ калькулятор.\n\
======================================================================================\n\
Доступные команды:\n\
Регистрация    - введите 1\n\
Вход в систему - введите 2\n\
Выход          - введите 0\n\
======================================================================================')
    comm1 = input('Ввод: ')
    if comm1 == '1':
        reg()
    elif comm1 == '2':
        vhod_v_sis()
    elif comm1 != '1' and comm1 != '2' and comm1 != '0':
        print('Неправильный символ!\n\
======================================================================================')
        vhod()
    elif comm1 == '0':
        print('Будьте здоровы! Всего доброго!')


def dobavit_p():
    name = input('Введите Ваше ФИО ')
    age = int(input('Введите Ваш возраст '))
    gender = input('Введите букву м если Вы мужчина, или букву ж если Вы женщина ')
    while gender != 'м' and gender != 'ж':
        print('Неправильный символ! ')
        gender = input('Введите букву м если Вы мужчина, или букву ж если Вы женщина ')
    height = int(input('Введите Ваш рост в см '))
    weight = int(input('Введите Ваш вес в кг '))
    list_p[name] = {
        'Возраст': age,
        'Пол': gender,
        'Рост': height,
        'Вес': weight,
    }
    with open('data_user.txt', 'w') as json_w:
        json.dump(list_p, json_w)
    raschet_bmi(weight, height, age, name, gender)
    menu()


def del_p():
    with open('data_user.txt', 'r') as json_read:
        list_p = json.load(json_read)
    if len(list_p) == 0:
        print('Список пуст, добавте пользователя - введите 2')
    else:
        name = input('Введите ФИО: ')
        with open('data_user.txt', 'r') as json_read:
            list_p = json.load(json_read)
        del (list_p[name])


def spis_p():
    with open('data_user.txt', 'r') as json_read:
        list_p = json.load(json_read)
    if len(list_p) == 0:
        print('Список пуст, добавте пользователя - введите 2')
    else:
        with open('data_user.txt', 'r') as json_read:
            list_p = json.load(json_read)
        for i in list_p:
            print(i)


def vybr_p():
    with open('data_user.txt', 'r') as json_read:
        list_p = json.load(json_read)
    if len(list_p) == 0:
        print('Список пуст, добавте пользователя - введите 2')
    else:
        with open('data_user.txt', 'r') as json_read:
            list_p = json.load(json_read)
        for i in list_p:
            print(i)
        with open('data_user.txt', 'r') as json_read:
            list_p = json.load(json_read)
        name = input('Введите ФИО из списка: ')
        print("ФИО: {}\nВозраст: {}\nПол: {}\nРост: {}\n\
Вес: {}".format(name, list_p[name]['Возраст'], list_p[name]['Пол'], list_p[name]['Рост'], list_p[name]['Вес']))
        upd = input('Обновить информацию? Введите да или нет: ')
        while upd != 'да' and upd != 'нет':
            print('Неправильный символ! ')
            upd = input('Обновить информацию? Введите да или нет: ')
        if upd == 'да':
            age = int(input('Возраст: '))
            gender = input('Пол м или ж: ')
            height = int(input('Рост в сантиметрах: '))
            weight = int(input('Вес: '))

            list_p.update({
                name: {
                    'Возраст': age,
                    'Пол': gender,
                    'Рост': height,
                    'Вес': weight,
                }

            })
            with open('data_user.txt', 'w') as json_w:
                json.dump(list_p, json_w)


def raschet_bmi(weight, height, age, name, gender):
    bmi = round((weight / (height / 100) ** 2), 2)
    recomm1 = 'У Вас недостаточная масса тела. Вам следует: кушать 5-6 раз в день, \n\
заняться спортом - силовые упрожнения для набора мышечной массы, \n\
пить воду за час до еды.'
    recomm2 = 'У Вас все впорядке. Так держать!'
    recomm3 = 'У Вас увеличенная масса тела.Вам следует: отказаться от вредных привычек, \n\
правильно умеренно питаться, заняться спортом - кардио нагрузки для сжигания жира, \n\
пить воду за пол часа до еды, высыпаться.'
    recomm4 = 'У Вас ожирение. Вам следует: отказаться от всего сладкого(быстрые углеводы), \n\
уменьшить приемы пищи, отказаться от вредных привычек, заняться спортом - \n\
кардио нагрузки для сжигания жира, пить воду за пол часа до еды, высыпаться, \n\
ОБРАТИТЬСЯ К ВРАЧУ-ДИЕТОЛОГУ!'
    if gender == 'м':
        print('Уважаемый ' + name + ', Ваш возраст - ' + str(age) + ', Ваш рост - ' + str(height) + 'см, Ваш \
вес - ' + str(weight) + 'кг, Ваш BMI - ' + str(bmi) + 'кг/м2')
    elif gender == 'ж':
        print('Уважаемая ' + name + ', Ваш возраст - ' + str(age) + ', Ваш рост - ' + str(height) + 'см, Ваш \
вес - ' + str(weight) + 'кг, Ваш BMI - ' + str(bmi) + 'кг/м2')
    if 18 < age <= 25:
        if gender == 'ж':
            if bmi <= 17:
                print(recomm1)
            if 17 < bmi <= 22:
                print(recomm2)
            if 22 < bmi <= 28:
                print(recomm3)
            if 28 < bmi:
                print(recomm4)
        elif gender == 'м':
            if bmi <= 17:
                print(recomm1)
            if 17 < bmi <= 23:
                print(recomm2)
            if 23 < bmi <= 29:
                print(recomm3)
            if 29 < bmi:
                print(recomm4)
    elif 25 < age:
        if gender == 'ж':
            if bmi <= 18:
                print(recomm1)
            if 18 < bmi <= 23:
                print(recomm2)
            if 23 < bmi <= 29:
                print(recomm3)
            if 29 < bmi:
                print(recomm4)
        elif gender == 'м':
            if bmi <= 18:
                print(recomm1)
            if 18 < bmi <= 24:
                print(recomm2)
            if 24 < bmi <= 30:
                print(recomm3)
            if 30 < bmi:
                print(recomm4)
    a1 = (bmi - 11)
    a2 = (69 - bmi)
    print('10' + '#' * round(a1) + str(bmi) + '.' * round(a2) + '70')


def menu():
    print('======================================================================================\n\
Меню:\n\
Доступные команды:\n\
Вывести список пользователей - введите 1\n\
Добавить пользователя        - введите 2\n\
Удалить пользователя         - введите 3\n\
Выбрать пользователя         - введите 4\n\
Выход                        - введите 0\n\
======================================================================================')
    comm = int(input('Ввод: '))
    if comm == 1:
        spis_p()
        return menu()
    elif comm == 2:
        dobavit_p()
    elif comm == 3:
        del_p()
        return menu()
    elif comm == 4:
        vybr_p()
        return menu()
    elif comm == 0:
        print('Будьте здоровы!!!')
        vhod()
    else:
        print('Неправильный символ! ')
        return menu()


vhod()
