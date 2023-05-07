# -*- coding: windows-1251 -*-

def Pirs(Tknf):
    Tknf = list(Tknf)  # ���������� � ������
    Tknf = [">" if x == "&" or x == "v" else x for x in Tknf]  # �������� ��� ����� �� ���������
    for i, val in enumerate(Tknf):  # ����������� �� ��������
        if val == "n":  # ���� ��������� �
            x_save = ''.join(Tknf[i + 1]) + Tknf[i + 2]  # ���� ��� � �����, ��� �
            del Tknf[i:i + 2]  # ������� nxX
            Tknf[i] = '(' + x_save + " > " + x_save + ')'  # �������� �������
    Tknf = ''.join(Tknf)  # ��������� � ������
    return Tknf  # ����������


def Sheffer(Tdnf):
    Tdnf = list(Tdnf)  # ��������� � ������
    Tdnf = ["/" if x == "^" or x == "v" else x for x in Tdnf]  # ������ �� �������� ��� �����
    for i, val in enumerate(Tdnf):  # ����������� �� ���������
        if val == "n":  # ��������� �
            x_save = ''.join(Tdnf[i + 1]) + Tdnf[i + 2]  # �������� ��� � ������
            del Tdnf[i:i + 2]  # ������� � � ��� � ������
            Tdnf[i] = '(' + x_save + " / " + x_save + ')'  # ������� �������
    Tdnf = ''.join(Tdnf)  # ������������� � ������
    return Tdnf  # �������


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
