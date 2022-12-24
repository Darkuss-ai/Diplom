# -*- coding: windows-1251 -*-
import sys

sys.path.append("..")
import unittest
import Qtable as Qt
import minimi as mini
import tablechecks as tcheck

offset = [0, 1, 2, 3, 4, 5, 6]
variants = [
    'a_true',
    'b_true',
    'c_true',
    'd_true',
    'e_true',
    'f_true',
    'g_true',
    'l_true',
    'm_true'
]


class QuaineTest(unittest.TestCase):

    def test_tables_DNF(self):

        for i in range(len(offset)):
            for j in range(len(variants)):
                my_var = Qt.create_var(Qt.dataframe[variants[j]], offset[i])
                my_var, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = Qt.modify_var(my_var, offset[i])
                Quine = mini.Kvaina_DNF(Fsdnf)
                test_b = list(my_var['b'])
                while 1:
                    temp = mini.Kvaina_DNF(Quine)
                    if temp == Quine:
                        break
                    else:
                        Quine = temp.copy()

                for k in range(len(Quine)):
                    Quine[k] = Quine[k].replace('^', ' ^ ')
                Quine = mini.format_DNF(Quine)
                split_check = tcheck.Split_Tdnf(Quine)
                test_table = tcheck.check_Tablе_tdnf(my_var, split_check)
                curr_b = list(test_table['b'])
                with self.subTest(i=i, j=j):
                    self.assertEqual(test_b, curr_b)
                    print('\n', test_b, '\n', curr_b, '\n\n')

    def test_tables_KNF(self):

        for i in range(len(offset)):
            for j in range(len(variants)):
                my_var = Qt.create_var(Qt.dataframe[variants[j]], offset[i])
                my_var, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = Qt.modify_var(my_var, offset[i])
                Quine = mini.Kvaina_KNF(Fsknf)
                test_b = list(my_var['b'])
                while 1:
                    temp = mini.Kvaina_KNF(Quine)
                    if temp == Quine:
                        break
                    else:
                        Quine = temp.copy()

                for k in range(len(Quine)):
                    Quine[k] = Quine[k].replace('v', ' v ')
                Quine = mini.format_KNF(Quine)
                split_check = tcheck.Split_Tknf(Quine)
                test_table = tcheck.check_Tablе_tknf(my_var, split_check)
                curr_b = list(test_table['b'])
                with self.subTest(i=i, j=j):
                    self.assertEqual(test_b, curr_b)
                    print('\n', test_b, '\n', curr_b, '\n\n')
