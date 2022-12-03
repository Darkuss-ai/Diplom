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

    K0 = []
    K1 = []
    K2 = []
    K3 = []
    K4 = []
    counter = 0

    if len(K00) > 0:
        for i in range(len(K00)):
            for j in range(len(K01)):
                if f.ratio(K00[i], K01[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K00[i])):
                        if K00[i][k] != K01[j][k]:
                            K1.append(''.join(K01[j][:k]) + 'x' + K01[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K01):
                    K0.append(K00[i])
        counter = 0
        for i in range(len(K01)):
            for j in range(len(K02)):
                if f.ratio(K01[i], K02[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            K2.append(''.join(K02[j][:k]) + 'x' + K02[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K02):
                    K0.append(K01[i])
        counter = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                if f.ratio(K02[i], K03[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            K3.append(''.join(K03[j][:k]) + 'x' + K03[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K03):
                    K0.append(K02[i])
        counter = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                if f.ratio(K03[i], K04[j]) >= 75 and f.partial_ratio(K03[i], K04[j]) < 80:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            K4.append(''.join(K04[j][:k]) + 'x' + K04[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K04):
                    K0.append(K03[i])




    elif len(K01) > 0:
        for i in range(len(K01)):
            for j in range(len(K02)):
                if f.ratio(K01[i], K02[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            K2.append(''.join(K02[j][:k]) + 'x' + K02[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K02):
                    K0.append(K01[i])
        counter = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                if f.ratio(K02[i], K03[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            K3.append(''.join(K03[j][:k]) + 'x' + K03[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K03):
                    K0.append(K02[i])
        counter = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                if f.ratio(K03[i], K04[j]) >= 75 and f.partial_ratio(K03[i], K04[j]) < 80:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            K4.append(''.join(K04[j][:k]) + 'x' + K04[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K04):
                    K0.append(K03[i])



    elif len(K02) > 0:
        for i in range(len(K02)):
            for j in range(len(K03)):
                if f.ratio(K02[i], K03[j]) >= 75 and f.partial_ratio(K02[i], K03[j]) < 80:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            K3.append(''.join(K03[j][:k]) + 'x' + K03[j][k + 1:])
                else:
                    counter += 1

                if counter == len(K03):
                    K0.append(K02[j])
        counter = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                if f.ratio(K03[i], K04[j]) >= 75 and f.partial_ratio(K03[i], K04[j]) < 80:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            K4.append(''.join(K04[j][:k]) + 'x' + K04[j][k + 1:])
                else:
                    counter += 1
                if counter == len(K04):
                    K0.append(K03[i])



    elif len(K03) > 0:
        for i in range(len(K03)):
            for j in range(len(K04)):
                if f.ratio(K03[i], K04[j]) >= 75 and f.partial_ratio(K03[i], K04[j]) < 80:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            K4.append(''.join(K04[j][:k]) + 'x' + K04[j][k + 1:])
                else:
                    counter += 1
                if counter == len(K04):
                    K0.append(K03[i])


    else:
        K1 = K1 + K04

    import itertools

    K0.sort()

    K0 = list(K0 for K0, _ in itertools.groupby(K0))
    counter = 0
    cube1 = K1 + K2 + K3 + K4
    for i in range(len(K0)):
        for j in range(len(cube1)):
            if f.ratio(cube1[j], K0[i]) >= 75:
                break
            else:
                counter += 1
        if counter == len(cube1):
            cube1.append(K0[i])

    K11 = []
    K12 = []
    K13 = []
    K14 = []

    for i in range(len(cube1)):
        if cube1[i][0] == 'x':
            K11.append(cube1[i])
        elif cube1[i][1] == 'x':
            K12.append(cube1[i])
        elif cube1[i][2] == 'x':
            K13.append(cube1[i])
        else:
            K14.append(cube1[i])

    print(K11)
    # print(K12)
    # print(K13)
    # print(K14)

    final = []
    test = []

    for i in range(len(K11)):
        if len(K11) == 1:
            final.append(K11[0])
            break
        for j in range(len(K11)):
            if i == j:
                continue
            if f.ratio(K11[i], K11[j]) >= 75:
                for k in range(len(K11[i])):
                    if K11[i][k] != K11[j][k]:
                        final.append(''.join(K11[j][:k]) + 'x' + K11[j][k + 1:])
            else:
                test.append(K11[i])

    for i in range(len(K12)):
        if len(K12) == 1:
            final.append(K12[0])
            break
        for j in range(len(K12)):
            if i == j:
                continue
            if f.ratio(K12[i], K12[j]) >= 75:
                for k in range(len(K12[i])):
                    if K12[i][k] != K12[j][k]:
                        final.append(''.join(K12[j][:k]) + 'x' + K12[j][k + 1:])
            else:
                test.append(K12[i])

    for i in range(len(K13)):
        if len(K13) == 1:
            final.append(K13[0])
            break
        for j in range(len(K13)):
            if i == j:
                continue
            if f.ratio(K13[i], K13[j]) >= 75:
                for k in range(len(K13[i])):
                    if K13[i][k] != K13[j][k]:
                        final.append(''.join(K13[j][:k]) + 'x' + K13[j][k + 1:])
            else:
                test.append(K13[i])

    for i in range(len(K14)):
        if len(K14) == 1:
            final.append(K14[0])
            break
        for j in range(len(K14)):
            if i == j:
                continue
            if f.ratio(K14[i], K14[j]) >= 75:
                for k in range(len(K14[i])):
                    if K14[i][k] != K14[j][k]:
                        final.append(''.join(K14[j][:k]) + 'x' + K14[j][k + 1:])
            else:
                test.append(K14[i])

    for i in range(len(test)):
        if test.count(test[i]) > 1:
            final.append(test[i])


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
            term = term + ' ^ '
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