# -*- coding: windows-1251 -*-

import itertools
from thefuzz import fuzz as f


def Kvaina_DNF(Fsdnf):
    for i in range(len(Fsdnf)):
        Fsdnf[i] = Fsdnf[i].replace(' ', '')
        Fsdnf[i] = Fsdnf[i].replace('(', '')
        Fsdnf[i] = Fsdnf[i].replace(')', '')
    term_list = [[""] * 0 for i in range(len(Fsdnf))]
    for i in range(len(Fsdnf)):
        term = Fsdnf[i]  # Берём первый терм
        for k in range(term.count('^') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('^')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list[i].append(term[:split])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list[i].append(term)  # Берём всё кроме скобок

    final_list = []
    nnn = term_list.copy()
    for i in range(len(nnn)):
        terms = nnn[i]
        for j in range(len(nnn)):
            if terms == nnn[j]:
                continue
            else:
                temp = terms.copy()
                if f.ratio(terms, nnn[j]) >= 97:
                    # print(terms, 'Минимизируется с ', term_list[j], '\n')
                    for k in range(len(terms)):
                        if (terms[k] != nnn[j][k]):
                            temp.pop(k)
                            term_list.append(temp)
                            final_list.append(terms)
                            break

    final_list.sort()

    final_list = list(final_list for final_list, _ in itertools.groupby(final_list))
    term_list.sort()
    term_list[:] = [x for x in term_list if x not in final_list]
    term_list = list(term_list for term_list, _ in itertools.groupby(term_list))

    ret = []
    for i in range(len(term_list)):
        ret.append('^'.join(term_list[i]))
    return (ret)


def Kvaina_KNF(Fsknf):
    for i in range(len(Fsknf)):
        Fsknf[i] = Fsknf[i].replace(' ', '')
        Fsknf[i] = Fsknf[i].replace('(', '')
        Fsknf[i] = Fsknf[i].replace(')', '')
    term_list = [[""] * 0 for i in range(len(Fsknf))]
    for i in range(len(Fsknf)):
        term = Fsknf[i]  # Берём первый терм
        for k in range(term.count('v') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('v')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list[i].append(term[:split])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list[i].append(term)  # Берём всё кроме скобок

    final_list = []
    nnn = term_list.copy()
    for i in range(len(nnn)):
        terms = nnn[i]
        for j in range(len(nnn)):
            if terms == nnn[j]:
                continue
            else:
                temp = terms.copy()
                if f.ratio(terms, nnn[j]) >= 97:
                    # print(terms, 'Минимизируется с ', term_list[j], '\n')
                    for k in range(len(terms)):
                        if (terms[k] != nnn[j][k]):
                            temp.pop(k)
                            term_list.append(temp)
                            final_list.append(terms)
                            break

    final_list.sort()

    final_list = list(final_list for final_list, _ in itertools.groupby(final_list))
    term_list.sort()
    term_list[:] = [x for x in term_list if x not in final_list]
    term_list = list(term_list for term_list, _ in itertools.groupby(term_list))

    ret = []
    for i in range(len(term_list)):
        ret.append('v'.join(term_list[i]))
    return (ret)


def Quine_McCluskey(function, ftype, my_var):
    zero_count = 0
    K00 = []
    K01 = []
    K02 = []
    K03 = []
    K04 = []
    for i in range(len(function)):
        if function[i].count('0') > zero_count:
            zero_count = function[i].count('0')
    if zero_count == 4:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K00.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K01.append(function[i])
            elif function[i].count('0') == zero_count - 2:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 3:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 3:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K01.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 2:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 2:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 1:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K03.append(function[i])
            else:
                K04.append(function[i])
    else:
        for i in range(len(function)):
            K04.append(function[i])

    K0 = K00.copy()
    K1 = K01.copy()
    K2 = K02.copy()
    K3 = K03.copy()
    cube1 = []
    counter = 0
    equal = 0

    if len(K00) > 0:
        for i in range(len(K00)):
            for j in range(len(K01)):
                for k in range(len(K00[i])):
                    if K00[i][k] != K01[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K00[i])):
                        if K00[i][k] != K01[j][k]:
                            cube1.append(''.join(K00[i][:k] + 'x' + K00[i][k + 1:]))
                            if K00[i] in K0:
                                K0.remove(K00[i])
                            if K01[j] in K1:
                                K1.remove(K01[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K01)):
            for j in range(len(K02)):
                for k in range(len(K01[i])):
                    if K01[i][k] != K02[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            cube1.append(''.join(K01[i][:k] + 'x' + K01[i][k + 1:]))
                            if K01[i] in K1:
                                K1.remove(K01[i])
                            if K02[j] in K2:
                                K2.remove(K02[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0


    elif len(K01) > 0:
        for i in range(len(K01)):
            for j in range(len(K02)):
                for k in range(len(K01[i])):
                    if K01[i][k] != K02[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            cube1.append(''.join(K01[i][:k] + 'x' + K01[i][k + 1:]))
                            if K01[i] in K1:
                                K1.remove(K01[i])
                            if K02[j] in K2:
                                K2.remove(K02[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    elif len(K02) > 0:
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    elif len(K03) > 0:
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    else:
        cube1 = K04

    K11, K12, K13, K14 = [], [], [], []

    cube1 += K0 + K1 + K2 + K3

    for i in range(len(cube1)):
        if cube1[i][0] == 'x':
            K11.append(cube1[i])
        elif cube1[i][1] == 'x':
            K12.append(cube1[i])
        elif cube1[i][2] == 'x':
            K13.append(cube1[i])
        else:
            K14.append(cube1[i])

    final = []
    test = []

    counter = 0
    for i in range(len(K11)):
        if len(K11) == 1:
            final.append(K11[0])
            break
        for j in range(len(K11)):
            if i == j:
                continue
            for k in range(len(K11[i])):
                if K11[i][k] != K11[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K11[i])):
                    if K11[i][k] != K11[j][k]:
                        final.append(''.join(K11[i][:k] + 'x' + K11[i][k + 1:]))
            else:
                counter = 0
                test.append(K11[i])

    counter = 0
    for i in range(len(K12)):
        if len(K12) == 1:
            final.append(K12[0])
            break
        for j in range(len(K12)):
            if i == j:
                continue
            for k in range(len(K12[i])):
                if K12[i][k] != K12[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K12[i])):
                    if K12[i][k] != K12[j][k]:
                        final.append(''.join(K12[i][:k] + 'x' + K12[i][k + 1:]))
            else:
                counter = 0
                test.append(K12[i])

    counter = 0
    for i in range(len(K13)):
        if len(K13) == 1:
            final.append(K13[0])
            break
        for j in range(len(K13)):
            if i == j:
                continue
            for k in range(len(K13[i])):
                if K13[i][k] != K13[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K13[i])):
                    if K13[i][k] != K13[j][k]:
                        final.append(''.join(K13[i][:k] + 'x' + K13[i][k + 1:]))
            else:
                counter = 0
                test.append(K13[i])

    counter = 0
    for i in range(len(K14)):
        if len(K14) == 1:
            final.append(K14[0])
            break
        for j in range(len(K14)):
            if i == j:
                continue
            for k in range(len(K14[i])):
                if K14[i][k] != K14[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K14[i])):
                    if K14[i][k] != K14[j][k]:
                        final.append(''.join(K14[i][:k] + 'x' + K14[i][k + 1:]))
            else:
                counter = 0
                test.append(K14[i])

    final += test

    import itertools
    final.sort()
    final = list(final for final, _ in itertools.groupby(final))

    ret_final = []
    term = ''
    for i in range(len(final)):
        for j in range(len(final[i])):
            if final[i][j] == '0' and ftype == 'DNF':
                term = term + 'n' + my_var.columns[j]
            elif final[i][j] == '0' and ftype == 'KNF':
                term = term + my_var.columns[j]
            elif final[i][j] == '1' and ftype == 'DNF':
                term = term + my_var.columns[j]
            elif final[i][j] == '1' and ftype == 'KNF':
                term = term + 'n' + my_var.columns[j]
            else:
                continue
            if ftype == 'DNF':
                term = term + ' ^ '
            else:
                term = term + ' v '
        term = term[:-3]
        ret_final.append(term)
        term = ''
    for i in range(len(ret_final)):
        ret_final[i] = ret_final[i].replace(" ", "")
    return ret_final


def format_DNF(NF):
    for i in range(len(NF)):
        NF[i] = '(' + NF[i] + ')'
    NF = ' v '.join(NF)
    return NF

def format_KNF(NF):
    for i in range(len(NF)):
        NF[i] = '(' + NF[i] + ')'
    NF = ' & '.join(NF)
    return NF
