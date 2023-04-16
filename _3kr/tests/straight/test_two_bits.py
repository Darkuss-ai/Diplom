import unittest
import sys

sys.path.append("../_3kr")
from _3kr import algorithms as algo


def calculate_bits(x_, y_):
    if x_ + y_ >= 16:
        return 9
    elif x_ + y_ >= 8:
        return 7
    elif x_ + y_ >= 4:
        return 5
    return 3


def change_bits(bits):
    if bits == ['0', '0']:
        return ['0', '1']
    elif bits == ['0', '1']:
        return ['1', '0']
    elif bits == ['1', '0']:
        return ['1', '1']
    else:
        return ['0', '0']


class two_bits(unittest.TestCase):

    def test_two_bits(self):
        for i in range(1, 50):
            for j in range(50):

                x = i
                y = j
                number_of_bits = calculate_bits(x, y)

                X = algo.convert(x, number_of_bits)
                Y = algo.convert(y, number_of_bits)
                minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)
                S = ['0' for m in range(len(X) * 2 - 1)]
                interval_left = len(Y) - 2
                interval_right = len(Y)
                corr = 0
                for l in range((len(Y) - 1) // 2):
                    two_bits = Y[interval_left:interval_right]
                    if corr == 1:
                        two_bits = change_bits(two_bits)
                        if two_bits == ["0", "0"]:
                            corr = 1
                        else:
                            corr = 0
                    if two_bits == ['0', '0']:
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
                    elif two_bits == ["0", '1']:
                        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
                    elif two_bits == ['1', '1']:
                        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
                        corr = 1
                    else:
                        new_X = algo.shift(X.copy(), 'str' if X[0] == '0' else 'rev', 1)
                        S = algo.addition(S, new_X.copy(), len(X) * 2 - 1, code='dop', kr=3)
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)

                    interval_left -= 2
                    interval_right -= 2

                if Y[0] == '0' and corr == 1:
                    S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
                elif Y[0] == '1' and corr == 1:
                    S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                elif Y[0] == "1" and corr == 0:
                    S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)

                if S[0] == '1':
                    S = algo.rev(algo.convert(S.copy(), len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j)
                    self.assertEqual(i * j, algo.convert(S))
