# -*- coding: windows-1251 -*-


def Split_Tdnf(Tdnf):
    print(Tdnf)
    tdnf_check = []  # ������� ������
    for i in range(Tdnf.count("v") + 1):  # �������, ������� ������ � ���������� 1 � ��������
        if (Tdnf.find('v') != -1):  # ���� ����� ����
            tdnf_check.append(Tdnf[:Tdnf.find("v") - 1])  # ��������� �� �� �����
            Tdnf = ''.join(Tdnf[Tdnf.find("v") + 2:])  # ������� ������
    else:  # ���� ��� �����
        tdnf_check.append(Tdnf)  # ������ ������� �� �� ���������� �����. ������ ����������
    return tdnf_check  # ����������


def Split_Tknf(Tknf):  # �� �� ����� ��� ���
    tknf_check = []  # ������
    for i in range(Tknf.count("&") + 1):  # �� ���������� ������ + 1
        if (Tknf.find('&') != -1):  # ���� �����
            tknf_check.append(Tknf[:Tknf.find("&") - 1])  # ���� �� �� ����
            Tknf = ''.join(Tknf[Tknf.find("&") + 2:])  # ���� �� ����� ���� � ������ ������
    else:  # ���� ������ ���
        tknf_check.append(Tknf)  # ������ ���������

    return tknf_check  # ����������

# ����� ����� ����������� ������� � �������� ������, ������� � �����. ����� � ��������� ������
# ��� ���� �������� �������, �� ������� ����� ��������� ������������ ����������� ��������

def check_Tabl�_tdnf(table, splitTdnf):
    table_changed = table.copy()  # ��������� �������, ����� �� �������� �
    names = []  # ����� ��� �������� ����� �������
    orders = []  # ����� ��� ����������������� ������� � ��������
    for i in range(len(splitTdnf)):  # ������� ������ �������������
        term_list = []  # ������ ������
        term = splitTdnf[i]  # ���� ������ ����
        for k in range(term.count('^') + 1):  # ����� �� ���������� ������ ����������� �����
            split = term.find('^')  # ���� ������� �����
            if (split != -1):  # ���� ����� ����
                term_list.append(term[1:split - 1])  # ���� �� �� ����� (����� ������ � ������ � �������)
                term = term[split + 1:]  # ������� �� �� ����� � ���� ��, ��� ��������
            else:  # ���� �� ������ ��� �����
                term_list.append(term[1:-1])  # ���� �� ����� ������
        term_list = dict.fromkeys(term_list, [])  # ��������� � �������
        keys = list(term_list)  # ���������� �����
        order = "KLMNOPRST"  # ������ � ���������� ��������
        name = '^'.join(keys)  # ��������� ����� (����) � ����� ���� ������ ����
        names.append(order[i] + '=' + name)  # �������� ��������
        orders.append(order[i])  # ���� ���� ����� �� ������
        for j in range(len(term_list)):  # ��� �� ������� ����
            col = keys[j]  # ���������� �������� �����
            term_list[col] = []  # �������� �������� ������ ��������
            for count in range(16):  # 16 �������� �����
                if (keys[j].find('n') != -1):  # ���� ���� ���������� nx ���-��
                    col = keys[j].replace("n", '')  # ������� ����� n � col
                    if table[col][count] == '1':  # ���� � ������� 1
                        term_list[keys[j]].append('0')  # �� ������ �� 0 (��������)
                    else:  # ���� �� 0
                        term_list[keys[j]].append('1')  # �� ������ 1
                else:  # ���� �� ����� n,
                    term_list[col].append(table[col][count])  # �� ��������� ��� ��� ����
        fin = []  # ��������� ������
        for l in range(16):  # 16 ��������
            fin.append(int(term_list[keys[0]][l]))  # ���������� �������� �� ������� �����
        for h in range(1, len(keys)):  # �� 1 (0 �� ��� ���������) �� ���������� ������
            for l in range(16):  # 16 �������� ���
                fin[l] = fin[l] & int(term_list[keys[h]][l])  # ��������� ���������
        table_changed[names[i]] = fin  # ������ ������� �� ���������� � �������
    name = 'b='
    name = name + 'v'.join(orders)  # ��������� �������� ���������� �������
    names.append(name)  # ��������� ����� ���
    fin = []  # ��������
    for l in range(16):  # 16 ��������
        fin.append(int(table_changed[names[0]][l]))  # ���� �������� ������� �������
    for h in range(1, len(names) - 1):  # ��� �� ���� �������� ���� �������
        for l in range(16):  # 16 ��������
            fin[l] = fin[l] | table_changed[names[h]][l]  # � ������ ��������� �������� ����� ����
    table_changed[names[len(names) - 1]] = fin  # ������ ��������� ������� � �������
    # table_changed.pop("����") # ������� �� ������� ������� ����
    # table_changed.pop("����") # � ����
    return table_changed  # ����������


# �� �� ����� � ��� ����. ����������� ������� ������ ��������� � ��� ����:

def check_Tabl�_tknf(table, splitTknf):
    table_changed = table.copy()  # ��������� �������, ����� �� �������� �
    names = []  # ����� ��� �������� ����� �������
    orders = []  # ������ ��� �������
    for i in range(len(splitTknf)):  # ������� ������ �������������
        term_list = []  # ������ ������
        term = splitTknf[i]  # ���� ������ ����
        for k in range(term.count('v') + 1):
            split = term.find('v')  # ���� ������� �����
            if (split != -1):  # ���� ���� ����
                term_list.append(term[1:split - 1])  # ���� �� �� ����� (����� ������ � ������ � �������)
                term = term[split + 1:]  # �������
            else:  # ���� ������ ���
                term_list.append(term[1:-1])  # ���� ��, ����� ������
        term_list = dict.fromkeys(term_list, [])  # ��������� � �������
        keys = list(term_list)  # ���������� �����

        order = "KLMNOPRST"  # ������ � ���������� ��������
        name = 'v'.join(keys)  # ��������� ������
        names.append(order[i] + '=' + name)  # �������� ��������
        orders.append(order[i])  # ��������� �����
        for j in range(len(term_list)):  # ��� �� ������� ����
            col = keys[j]  # ���������� �������� �����
            term_list[col] = []  # �������� �������� ������ ��������
            for count in range(16):  # 16 �������� �����
                if (keys[j].find('n') != -1):  # ���� ���� ���������� nx ���-��
                    col = keys[j].replace("n", '')  # ������� ����� n � col
                    if table[col][count] == '1':  # ���� � ������� 1
                        term_list[keys[j]].append('0')  # �� ������ �� 0 (��������)
                    else:  # ���� �� 0
                        term_list[keys[j]].append('1')  # �� ������ 1
                else:  # ���� �� ����� n,
                    term_list[col].append(table[col][count])  # �� ��������� ��� ��� ����
        fin = []  # ��������� ������
        for l in range(16):  # 16 ��������
            fin.append(int(term_list[keys[0]][l]))  # ������ ���� - ��� ��������
        for h in range(1, len(keys)):  # �� ���� ������ ����� �������
            for l in range(16):  # 16 ��������
                fin[l] = fin[l] | int(term_list[keys[h]][l])  # ��������� ��������
        table_changed[names[i]] = fin  # ������ ������� �� ���������� � �������
    name = 'b='
    name = name + '&'.join(orders)  # ��������� �������� ���������� �������
    names.append(name)  # ��������� ����� ���
    fin = []  # ��������
    for l in range(16):  # 16 ��������
        fin.append(int(table_changed[names[0]][l]))  # ���� �������� ������� ��������
    for h in range(1, len(names) - 1):  # ��� �������� �� ��������, ����� �������
        for l in range(16):  # 16 ��������
            fin[l] = fin[l] & table_changed[names[h]][l]  # ��������� ��������� ����� ����
    table_changed[names[len(names) - 1]] = fin  # ������ ��������� ������� � �������
    # table_changed.pop("����") # ������� �� ������� ������� ����
    # table_changed.pop("����") # � ����
    return table_changed  # ����������


def Split_Pirs(Tknf_pirs):
    tknf_check = []  # ������� ������
    for i in range(Tknf_pirs.count(") > (") + 1):  # �������, ������� ������ � ���������� 1 � ��������
        if (Tknf_pirs.find(') > (') != -1):  # ���� ����� ����
            tknf_check.append(Tknf_pirs[:Tknf_pirs.find(") > (") + 1])  # ��������� �� �� �����
            Tknf_pirs = ''.join(Tknf_pirs[Tknf_pirs.find(") > (") + 4:])  # ������� ������
    else:  # ���� ��� �����
        tknf_check.append(Tknf_pirs)  # ������ ������� �� �� ���������� �����. ������ ����������
    return tknf_check  # ����������


def Split_Sheffer(Tdnf_sheffer):
    tdnf_check = []  # ������� ������
    for i in range(Tdnf_sheffer.count(") / (") + 1):  # �������, ������� ������ � ���������� 1 � ��������
        if Tdnf_sheffer.find(') / (') != -1:
            tdnf_check.append(Tdnf_sheffer[:Tdnf_sheffer.find(") / (") + 1])  # ��������� �� �� �����
            Tdnf_sheffer = ''.join(Tdnf_sheffer[Tdnf_sheffer.find(") / (") + 4:])  # ������� ������
    else:  # ���� ��� �����
        tdnf_check.append(Tdnf_sheffer)  # ������ ������� �� �� ���������� �����. ������ ����������
        # print(tdnf_check)
    return tdnf_check  # ����������


def check_Tabl�_Pirs(table, Tknf_pirs, table1):
    # print(pirs)
    pirs = Split_Pirs(Tknf_pirs)
    table_changed = table.copy()  # ��������� �������, ����� �� �������� �
    names = []  # ����� ��� �������� ����� �������
    orders = []  # ����� ��� ����������������� ������� � ��������
    for i in range(len(pirs)):  # ������� ������ �������������
        term_list = []  # ������ ������
        term = pirs[i]  # ���� ������ ����
        for k in range(term.count('>') + 1):  # ����� �� ���������� ������ ����������� �����
            split = term.find('>')  # ���� ������� �����
            if (split != -1):  # ���� ����� ����
                term_list.append(term[1:split - 1])  # ���� �� �� ����� (����� ������ � ������ � �������)
                term = term[split + 1:]  # ������� �� �� ����� � ���� ��, ��� ��������
            else:  # ���� �� ������ ��� �����
                term_list.append(term[1:-1])  # ���� �� ����� ������
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # ��������� � �������
        keys = list(term_list)  # ���������� �����
        order = "KLMNOPRST"  # ������ � ���������� ��������
        name = '>'.join(keys)  # ��������� ����� (����) � ����� ���� ������ ����
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # �������� ��������
        orders.append(order[i])  # ���� ���� ����� �� ������
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # ��� �� ������� ����
            col = keys[j]  # ���������� �������� �����
            term_list[col] = []  # �������� �������� ������ ��������
            for count in range(16):  # 16 �������� �����
                term_list[col].append(table[col][count])  # �� ��������� ��� ��� ����
        fin = []  # ��������� �����f
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 ��������
                fin.append(int(term_list[keys[-1]][l]))  # ������ ���� - ��� ��������
            # for h in range(len(keys)-1, -4, -1): # �� ���� ������ ����� �������
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 ��������
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # ��������� ��������
        else:
            for l in range(16):  # 16 ��������
                fin.append(int(term_list[keys[0]][l]))  # ������ ���� - ��� ��������
            for h in range(1, len(keys)):  # �� ���� ������ ����� �������
                for l in range(16):  # 16 ��������
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # ��������� ��������
        table_changed[names[i]] = fin  # ������ ������� �� ���������� � �������
    name = 'b='
    name = name + '//'.join(orders)  # ��������� �������� ���������� �������
    names.append(name)  # ��������� ����� ���

    final_col = []
    final_col = (table1.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # ������ ��������� ������� � �������
    # table_changed.pop("����") # ������� �� ������� ������� ����
    # table_changed.pop("����") # � ����
    return table_changed  # ����������


def check_Tabl�_Sheffer(table, Tdnf_sheffer, table1):
    # print(pirs)
    sheffer = Split_Sheffer(Tdnf_sheffer)
    table_changed = table.copy()  # ��������� �������, ����� �� �������� �
    names = []  # ����� ��� �������� ����� �������
    orders = []  # ����� ��� ����������������� ������� � ��������
    for i in range(len(sheffer)):  # ������� ������ �������������
        term_list = []  # ������ ������
        term = sheffer[i]  # ���� ������ ����
        for k in range(term.count('/') + 1):  # ����� �� ���������� ������ ����������� �����
            split = term.find('/')  # ���� ������� �����
            if (split != -1):  # ���� ����� ����
                term_list.append(term[1:split - 1])  # ���� �� �� ����� (����� ������ � ������ � �������)
                term = term[split + 1:]  # ������� �� �� ����� � ���� ��, ��� ��������
            else:  # ���� �� ������ ��� �����
                term_list.append(term[1:-1])  # ���� �� ����� ������
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # ��������� � �������
        keys = list(term_list)  # ���������� �����
        order = "KLMNOPRST"  # ������ � ���������� ��������
        name = '/'.join(keys)  # ��������� ����� (����) � ����� ���� ������ ����
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # �������� ��������
        orders.append(order[i])  # ���� ���� ����� �� ������
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # ��� �� ������� ����
            col = keys[j]  # ���������� �������� �����
            term_list[col] = []  # �������� �������� ������ ��������
            for count in range(16):  # 16 �������� �����
                term_list[col].append(table[col][count])  # �� ��������� ��� ��� ����
        fin = []  # ��������� �����f
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 ��������
                fin.append(int(term_list[keys[-1]][l]))  # ������ ���� - ��� ��������
            # for h in range(len(keys)-1, -4, -1): # �� ���� ������ ����� �������
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 ��������
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # ��������� ��������
        else:
            for l in range(16):  # 16 ��������
                fin.append(int(term_list[keys[0]][l]))  # ������ ���� - ��� ��������
            for h in range(1, len(keys)):  # �� ���� ������ ����� �������
                for l in range(16):  # 16 ��������
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # ��������� ��������
        table_changed[names[i]] = fin  # ������ ������� �� ���������� � �������
    name = 'b='
    name = name + '/'.join(orders)  # ��������� �������� ���������� �������
    names.append(name)  # ��������� ����� ���

    final_col = []
    final_col = (table1.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # ������ ��������� ������� � �������
    # table_changed.pop("����") # ������� �� ������� ������� ����
    # table_changed.pop("����") # � ����
    return table_changed  # ����������

