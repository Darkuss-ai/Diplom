# -*- coding: windows-1251 -*-
import pandas as pd

trues = {
    'a_true': ['1', '0', '0', '0', '1', '1', '0', '0', '1', '1'],
    'b_true': ['1', '0', '1', '1', '0', '1', '0', '1', '1', '1'],
    'c_true': ['1', '1', '1', '0', '1', '0', '0', '0', '1', '1'],
    'd_true': ['1', '1', '0', '0', '1', '1', '1', '0', '1', '0'],
    'e_true': ['1', '0', '1', '0', '0', '1', '1', '0', '1', '0'],
    'f_true': ['1', '0', '0', '0', '0', '0', '1', '1', '1', '0'],
    'g_true': ['0', '0', '0', '1', '1', '1', '1', '0', '1', '1'],
    'l_true': ['0', '1', '0', '1', '0', '0', '1', '1', '0', '0'],
    'm_true': ['0', '0', '1', '1', '0', '0', '0', '0', '0', '1']
}

dataframe = pd.DataFrame(trues)


def create_var(b, offset):

    ix = {'x1': ['0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
          'x2': ['0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1'],
          'x3': ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1'],
          'x4': ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']}
    target = {'b': []}
    for i in range(offset):
        target['b'].append('x')
    for i in range(len(b)):
        target['b'].append(b[i])
    while len(target['b']) != 16:
        target['b'].append('x')
    final = pd.DataFrame.from_dict(ix)
    final['b'] = target['b']
    return final


def modify_str(func, t_func):  # ??????? ????????? ??????. ?????? ???? ? ??????? ?? ????????? ???????????
    func = list(func)  # ????????? ??????? ? ??????
    if t_func == 'SDNF':  # ???? ????
        for i in range(4):  # 4 ?????
            if func[i] == '0':  # ???? ? ??? ?????, ??
                func[i] = ' nx' + str(i + 1) + ' ^'  # ????? ?? ??? i+1. ? ??? ?? ? ????, ? ??? ? x1.
            else:  # ?????, ???? ? ??? 1
                func[i] = ' x' + str(i + 1) + ' ^'  # ?????? ???. ? ????? ????????? ???? ?????????
    else:  # ???? ?? ????
        for i in range(4):  # 4 ?????
            if func[i] == '0':  # ???? ????
                func[i] = ' nx' + str(i + 1) + ' v'  # ?????? ?? ?? ?????, ??? ?? ?????????? ???????
            else:  # ???? 1
                func[i] = ' x' + str(i + 1) + ' v'  # ?? ?? ?????, ??? ? ????, ?????? ? ????? ???? ????????

    func = ''.join(func)  # ????????? ? ??????
    return func  # ??????????


def modify_var(var_table, offset):
    SDKNF = {'����': [], '����': []}
    Fsdnf, Fsknf = [], []
    for i in range(16):
        SDKNF['����'].append('-')
        SDKNF['����'].append('-')
    var_table['����'] = SDKNF['����']
    var_table['����'] = SDKNF['����']
    func = ''
    func_list_DNF = []
    func_list_KNF = []
    for i in range(offset, offset + 10):
        if var_table['b'][i] == '1':
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_DNF.append(func)
            func = modify_str(func, 'SDNF')
            func = list(func)
            func.pop()
            func.append(")")
            func.insert(0, '(')
            func = ''.join(func)
            var_table.at[i, '����'] = func
            Fsdnf.append(func)
        else:
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_KNF.append(func)
            func = list(func)
            for j in range(4):
                if (func[j] == '0'):
                    func[j] = '1'
                else:
                    func[j] = '0'
            func = modify_str(func, 'SKNF')
            func = list(func)
            func.pop()
            func.append(")")
            func.insert(0, '(')
            func = ''.join(func)
            var_table.at[i, '����'] = func
            Fsknf.append(func)
    return var_table, Fsdnf, Fsknf, func_list_DNF, func_list_KNF