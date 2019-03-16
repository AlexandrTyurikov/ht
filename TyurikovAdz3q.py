lp = {}
a = 1
age = float
gender = input
height = float
weight = float
while a != 0:
    print('Доступные команды:\nВывести список пользователей - введите 1\n\
Добавить пользователя        - введите 2\n\
Удалить пользователя         - введите 3\nВыбрать пользователя         - введите 4\n\
Выход                        - введите 0')
    comm = int(input('Ввод: '))
    if comm == 1:
        if len(lp) == 0:
            print('Список пуст, добавте пользователя - введите 2')
        else:
            for i in lp:
                print(i)
    elif comm == 2:
        name = input('Введите Ваше ФИО ')
        age = int(input('Введите Ваш возраст '))
        gender = input('Введите букву м если Вы мужчина, или букву ж если Вы женщина ')
        height = int(input('Введите Ваш рост в сантиметрах '))
        weight = int(input('Введите Ваш вес '))
        lp[name] = {
            'Возраст': age,
            'Пол': gender,
            'Рост': height,
            'Вес': weight,
        }
    elif comm == 3:
        if len(lp) == 0:
            print('Список пуст, добавте пользователя - введите 2')
        else:
            name = input('Введите ФИО: ')
            del (lp[name])
    elif comm == 4:
        if len(lp) == 0:
            print('Список пуст, добавте пользователя - введите 2')
        else:
            name = input('Введите ФИО: ')
            print("ФИО: {}\nВозраст: {}\nПол: {}\nРост: {}\n\
Вес: {}".format(name, lp[name]['Возраст'], lp[name]['Пол'], lp[name]['Рост'], lp[name]['Вес']))
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
            g = '0----20____40^^^^60****80'
            if 0 < bmi < 7:
                q1 = g[:2] + str(bmi) + g[2:]
                print(q1)
            elif 7 <= bmi <= 14:
                q1 = g[:3] + str(bmi) + g[3:]
                print(q1)
            elif 14 < bmi < 20:
                q1 = g[:4] + str(bmi) + g[4:]
                print(q1)
            elif bmi == 20:
                print(g)
            elif 20 < bmi < 27:
                q1 = g[:8] + str(bmi) + g[8:]
                print(q1)
            elif 27 <= bmi <= 34:
                q1 = g[:9] + str(bmi) + g[9:]
                print(q1)
            elif 34 < bmi < 40:
                q1 = g[:10] + str(bmi) + g[10:]
                print(q1)
            elif bmi == 40:
                print(g)
            elif 40 < bmi < 47:
                q1 = g[:14] + str(bmi) + g[14:]
                print(q1)
            elif 47 <= bmi <= 54:
                q1 = g[:15] + str(bmi) + g[15:]
                print(q1)
            elif 54 < bmi < 60:
                q1 = g[:16] + str(bmi) + g[16:]
                print(q1)
            elif bmi == 60:
                print(g)
            elif 60 < bmi < 67:
                q1 = g[:20] + str(bmi) + g[20:]
                print(q1)
            elif 67 <= bmi <= 74:
                q1 = g[:21] + str(bmi) + g[21:]
                print(q1)
            elif 74 < bmi < 80:
                q1 = g[:22] + str(bmi) + g[22:]
                print(q1)

            upd = input('Обновить информацию? Введите да или нет: ')
            if upd == 'да':
                age = float(input('Возраст: '))
                gender = input('Пол м или ж: ')
                height = float(input('Рост в сантиметрах: '))
                weight = float(input('Вес: '))
                lp.update({
                    name:
                        {
                            'Возраст': age,
                            'Пол': gender,
                            'Рост': height,
                            'Вес': weight,
                        }
                })
    elif comm == 0:
        print('Будьте здоровы!!!')
        a = 0