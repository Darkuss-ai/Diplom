# -*- coding: windows-1251 -*-

def Pirs(Tknf):
    Tknf = list(Tknf)  # Превартили в список
    Tknf = [">" if x == "&" or x == "v" else x for x in Tknf]  # Заменили все знаки на стрелочку
    for i, val in enumerate(Tknf):  # Пробегаемся по символам
        if val == "n":  # Если встретили н
            x_save = ''.join(Tknf[i + 1]) + Tknf[i + 2]  # Берём икс и цифру, без н
            del Tknf[i:i + 2]  # удаляем nxX
            Tknf[i] = '(' + x_save + " > " + x_save + ')'  # собираем строчку
    Tknf = ''.join(Tknf)  # переводим в строку
    return Tknf  # возвращаем


def Sheffer(Tdnf):
    Tdnf = list(Tdnf)  # переводим в список
    Tdnf = ["/" if x == "^" or x == "v" else x for x in Tdnf]  # меняем на чёрточку все знаки
    for i, val in enumerate(Tdnf):  # пробегаемся по значениям
        if val == "n":  # встретили н
            x_save = ''.join(Tdnf[i + 1]) + Tdnf[i + 2]  # записали икс с цифрой
            del Tdnf[i:i + 2]  # удалили н и икс с цифрой
            Tdnf[i] = '(' + x_save + " / " + x_save + ')'  # Собрали строчку
    Tdnf = ''.join(Tdnf)  # преобразовали в строку
    return Tdnf  # вернули


def format_spaces_DNF(Tdnf):
    Tdnf = list(Tdnf)
    new_Tdnf = []
    for i in range(len(Tdnf)):
        if Tdnf[i] == '^':
            new_Tdnf.append(" ^ ")
        else:
            new_Tdnf.append(Tdnf[i])
    new_Tdnf = ''.join(new_Tdnf)
    return new_Tdnf


def format_spaces_KNF(Tknf):
    Tknf = list(Tknf)
    new_Tknf = []
    for i in range(len(Tknf)):
        if Tknf[i] == 'v':
            new_Tknf.append(" v ")
        else:
            new_Tknf.append(Tknf[i])
    new_Tdnf = ''.join(new_Tknf)
    return new_Tdnf
