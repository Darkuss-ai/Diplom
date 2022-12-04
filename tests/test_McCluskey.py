# -*- coding: windows-1251 -*-
import unittest
import Qtable as Qt
import minimi as mini
import basises as bases
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


class McCluskeyTest(unittest.TestCase):

    def test_tables_DNF(self):

        for i in range(len(offset)):
            for j in range(len(variants)):
                my_var = Qt.create_var(Qt.dataframe[variants[j]], offset[i])
                my_var, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = Qt.modify_var(my_var, offset[i])
                QuMcDNF = mini.Quine_McCluskey(func_list_DNF, 'DNF', my_var)
                test_b = list(my_var['b'])
                QuineMC_DNF = mini.format_DNF(QuMcDNF)
                QuineMC_DNF = bases.format_spaces_DNF(QuineMC_DNF)
                split_check = tcheck.Split_Tdnf(QuineMC_DNF)
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
                QuMcKNF = mini.Quine_McCluskey(func_list_KNF, 'KNF', my_var)
                test_b = list(my_var['b'])
                QuineMC_KNF = mini.format_KNF(QuMcKNF)
                QuineMC_KNF = bases.format_spaces_KNF(QuineMC_KNF)
                split_check = tcheck.Split_Tknf(QuineMC_KNF)
                test_table = tcheck.check_Tablе_tknf(my_var, split_check)
                curr_b = list(test_table['b'])
                with self.subTest(i=i, j=j):
                    self.assertEqual(test_b, curr_b)
                    print('\n', test_b, '\n', curr_b, '\n\n')
