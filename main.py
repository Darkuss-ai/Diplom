# -*- coding: windows-1251 -*-

import transfer as trans
import Qtable as Qt
import basises as bases
import tablechecks as tcheck
import minimi as mini

a = 32525.21355
a_dvoich, a_dvoich_whole, a_dvoich_frac = trans.from10to2(a, 9)
print(a)
print(a_dvoich)
a_oct = trans.from10to8(a, a_dvoich_whole, a_dvoich_frac)
print(a_oct)
a_hex = trans.from10to16(a, a_dvoich_whole, a_dvoich_frac)
print(a_hex)

print("\n\n")

print(trans.from10(720, 2))
print(trans.from2(1011010000, 7))
print(trans.fromP(2046, 7, 3))

offset = 5
variant = 'b_true'
my_var = Qt.create_var(Qt.dataframe[variant], offset)
print(my_var)

my_var_save = my_var.copy()
my_var, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = Qt.modify_var(my_var, offset)
print("Fсднф = ", Fsdnf, '\n\n', "Fскнф = ", Fsknf)

print(my_var)

Tdnf = "(x1 ^ nx4) v (x2 ^ x4)"
Tknf = "(x1 v x4) & (x2 v nx4)"

Tknf_pirs = bases.Pirs(Tknf)
Tdnf_sheffer = bases.Sheffer(Tdnf)

print(Tknf_pirs)
print(Tdnf_sheffer)

splitTdnf = tcheck.Split_Tdnf(Tdnf)  # Присваиваем
splitTknf = tcheck.Split_Tknf(Tknf)  # Присваиваем

table1 = tcheck.check_Tablе_tdnf(my_var_save, splitTdnf) # Запоминаем первую таблицу СДНФ
table2 = tcheck.check_Tablе_tknf(my_var_save, splitTknf) # Запоминаем вторую таблицу СКНФ


print(table1)
print(table2)

chkPirs = tcheck.check_Tablе_Pirs(my_var_save, Tknf_pirs, table1)
chkSheffer = tcheck.check_Tablе_Sheffer(my_var_save, Tdnf_sheffer, table1)

print(chkPirs)
print(chkSheffer)


Quine = mini.Kvaina_DNF(Fsdnf)
while 1:
    temp = mini.Kvaina_DNF(Quine)
    if temp == Quine:
        break
    else:
        Quine = temp.copy()

for i in range(len(Quine)):
    Quine[i] = Quine[i].replace('^', ' ^ ')
Quine = mini.format_DNF(Quine)
split_check = tcheck.Split_Tdnf(Quine)
print(tcheck.check_Tablе_tdnf(my_var_save, split_check))



Quine_KNF = mini.Kvaina_KNF(Fsknf)
while 1:
    temp = mini.Kvaina_KNF(Quine_KNF)
    if temp == Quine_KNF:
        break
    else:
        Quine_KNF = temp.copy()

for i in range(len(Quine_KNF)):
    Quine_KNF[i] = Quine_KNF[i].replace('v', ' v ')
Quine_KNF = mini.format_KNF(Quine_KNF)
split_check_knf = tcheck.Split_Tknf(Quine_KNF)
print(tcheck.check_Tablе_tknf(my_var_save, split_check_knf))


print("\n", func_list_DNF)
print("\n", func_list_KNF)
QuMcDNF = mini.Quine_McCluskey(func_list_DNF, 'DNF', my_var)
QuMcKNF = mini.Quine_McCluskey(func_list_KNF, 'KNF', my_var)
print("\n", QuMcDNF)
print("\n", QuMcKNF)