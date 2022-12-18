import pytest
import Qtable as Qt

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
DNF = ''
KNF = ''
testttt = []


def lol():
    for i in range(len(variants)):
        for j in range(len(offset)):
            my_var = Qt.create_var(Qt.dataframe[variants[i]], offset[j])
            my_var, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = Qt.modify_var(my_var, offset[j])
            DNF = "cat"
            KNF = "cat"


lol()

print(DNF)
print(KNF)
DNF = ['0010', '1010']
KNF = ['0000', '0111']
print(DNF)
for i in range(len(DNF)):
    print(DNF)
    @pytest.mark.parametrize("DNF", DNF)
    @pytest.mark.parametrize("KNF", KNF)
    def test_passing(DNF, KNF):
        assert DNF != KNF
        print(DNF)
