# -*- coding: windows-1251 -*-


def Split_Tdnf(Tdnf):
    print(Tdnf)
    tdnf_check = []  # создали список
    for i in range(Tdnf.count("v") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if (Tdnf.find('v') != -1):  # если нашли знак
            tdnf_check.append(Tdnf[:Tdnf.find("v") - 1])  # добавляем всё до знака
            Tdnf = ''.join(Tdnf[Tdnf.find("v") + 2:])  # Срезаем строку
    else:  # Если нет знака
        tdnf_check.append(Tdnf)  # Значит срезали всё до последнего терма. ПРосто прибавляем
    return tdnf_check  # Возвраащем


def Split_Tknf(Tknf):  # То же самое для КНФ
    tknf_check = []  # Список
    for i in range(Tknf.count("&") + 1):  # До количества знаков + 1
        if (Tknf.find('&') != -1):  # Если нашли
            tknf_check.append(Tknf[:Tknf.find("&") - 1])  # Берём всё до него
            Tknf = ''.join(Tknf[Tknf.find("&") + 2:])  # Берём всё после него и взятых термов
    else:  # Если больше нет
        tknf_check.append(Tknf)  # Просто прибавяем

    return tknf_check  # Возвращаем

# Далее идуит проверочные таблицы в основном базисе, Щеффера и Пирса. Начнём с основного базиса
# Нам надо получить таблицу, по которой можно проверить правильность выполненных действий

def check_Tablе_tdnf(table, splitTdnf):
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(splitTdnf)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = splitTdnf[i]  # Берём первый терм
        for k in range(term.count('^') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('^')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list.append(term[1:-1])  # Берём всё кроме скобок
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '^'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                if (keys[j].find('n') != -1):  # Если ключ называется nx что-то
                    col = keys[j].replace("n", '')  # Убираем букву n у col
                    if table[col][count] == '1':  # Если в таблице 1
                        term_list[keys[j]].append('0')  # То меняем на 0 (Инверсия)
                    else:  # Если же 0
                        term_list[keys[j]].append('1')  # То ставим 1
                else:  # Если не нашли n,
                    term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборка
        for l in range(16):  # 16 значений
            fin.append(int(term_list[keys[0]][l]))  # запоминаем значения по первому ключу
        for h in range(1, len(keys)):  # От 1 (0 мы уже запомнили) до количества ключей
            for l in range(16):  # 16 значений там
                fin[l] = fin[l] & int(term_list[keys[h]][l])  # ПОбитовое умножение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = 'b='
    name = name + 'v'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя
    fin = []  # Обнуляем
    for l in range(16):  # 16 значений
        fin.append(int(table_changed[names[0]][l]))  # Берём значения первого столбца
    for h in range(1, len(names) - 1):  # Идём по всем столбцам крое первого
        for l in range(16):  # 16 значений
            fin[l] = fin[l] | table_changed[names[h]][l]  # И делаем побитовое сложение между ними
    table_changed[names[len(names) - 1]] = fin  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


# То же самое и для СКНФ. Комментарии прошлой фунции актуальны и для этой:

def check_Tablе_tknf(table, splitTknf):
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Массив для буковок
    for i in range(len(splitTknf)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = splitTknf[i]  # Берём первый терм
        for k in range(term.count('v') + 1):
            split = term.find('v')  # Ищем позицию знака
            if (split != -1):  # Если есть знак
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем
            else:  # Если больше нет
                term_list.append(term[1:-1])  # Берём всё, кроме скобок
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи

        order = "KLMNOPRST"  # Список с названиями столбцов
        name = 'v'.join(keys)  # ФОрмируем строку
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Добавляем букву
        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                if (keys[j].find('n') != -1):  # Если ключ называется nx что-то
                    col = keys[j].replace("n", '')  # Убираем букву n у col
                    if table[col][count] == '1':  # Если в таблице 1
                        term_list[keys[j]].append('0')  # То меняем на 0 (Инверсия)
                    else:  # Если же 0
                        term_list[keys[j]].append('1')  # То ставим 1
                else:  # Если не нашли n,
                    term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборка
        for l in range(16):  # 16 значений
            fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
        for h in range(1, len(keys)):  # По всем ключам кроме первого
            for l in range(16):  # 16 значений
                fin[l] = fin[l] | int(term_list[keys[h]][l])  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = 'b='
    name = name + '&'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя
    fin = []  # Обнуляем
    for l in range(16):  # 16 значений
        fin.append(int(table_changed[names[0]][l]))  # Берём значения первого столбика
    for h in range(1, len(names) - 1):  # Все значения из столбцов, кроме первого
        for l in range(16):  # 16 значений
            fin[l] = fin[l] & table_changed[names[h]][l]  # Побитовое умножение между ними
    table_changed[names[len(names) - 1]] = fin  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


def Split_Pirs(Tknf_pirs):
    tknf_check = []  # создали список
    for i in range(Tknf_pirs.count(") > (") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if (Tknf_pirs.find(') > (') != -1):  # если нашли знак
            tknf_check.append(Tknf_pirs[:Tknf_pirs.find(") > (") + 1])  # добавляем всё до знака
            Tknf_pirs = ''.join(Tknf_pirs[Tknf_pirs.find(") > (") + 4:])  # Срезаем строку
    else:  # Если нет знака
        tknf_check.append(Tknf_pirs)  # Значит срезали всё до последнего терма. ПРосто прибавляем
    return tknf_check  # Возвраащем


def Split_Sheffer(Tdnf_sheffer):
    tdnf_check = []  # создали список
    for i in range(Tdnf_sheffer.count(") / (") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if Tdnf_sheffer.find(') / (') != -1:
            tdnf_check.append(Tdnf_sheffer[:Tdnf_sheffer.find(") / (") + 1])  # добавляем всё до знака
            Tdnf_sheffer = ''.join(Tdnf_sheffer[Tdnf_sheffer.find(") / (") + 4:])  # Срезаем строку
    else:  # Если нет знака
        tdnf_check.append(Tdnf_sheffer)  # Значит срезали всё до последнего терма. ПРосто прибавляем
        # print(tdnf_check)
    return tdnf_check  # Возвраащем


def check_Tablе_Pirs(table, Tknf_pirs, table1):
    # print(pirs)
    pirs = Split_Pirs(Tknf_pirs)
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(pirs)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = pirs[i]  # Берём первый терм
        for k in range(term.count('>') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('>')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list.append(term[1:-1])  # Берём всё кроме скобок
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '>'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборкf
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[-1]][l]))  # Первый ключ - все значения
            # for h in range(len(keys)-1, -4, -1): # По всем ключам кроме первого
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # Побитовое сложение
        else:
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
            for h in range(1, len(keys)):  # По всем ключам кроме первого
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = 'b='
    name = name + '//'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя

    final_col = []
    final_col = (table1.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


def check_Tablе_Sheffer(table, Tdnf_sheffer, table1):
    # print(pirs)
    sheffer = Split_Sheffer(Tdnf_sheffer)
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(sheffer)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = sheffer[i]  # Берём первый терм
        for k in range(term.count('/') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('/')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list.append(term[1:-1])  # Берём всё кроме скобок
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '/'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборкf
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[-1]][l]))  # Первый ключ - все значения
            # for h in range(len(keys)-1, -4, -1): # По всем ключам кроме первого
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # Побитовое сложение
        else:
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
            for h in range(1, len(keys)):  # По всем ключам кроме первого
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = 'b='
    name = name + '/'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя

    final_col = []
    final_col = (table1.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем

