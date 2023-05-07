import unittest
import sys

sys.path.append("../_3kr")
from _3kr import algorithms as algo


def calculate_bits(x_, y_):
    if abs(x_) + abs(y_) >= 16:
        return 6
    elif abs(x_) + abs(y_) >= 8:
        return 5
    elif abs(x_) + abs(y_) >= 4:
        return 4
    return 4


class Boota(unittest.TestCase):

    def test_Boota(self):
        for i in range(8, 31):
            for j in range(16):
                number_of_bits = calculate_bits(i, j)
                X = algo.convert(i, number_of_bits)
                Y = algo.convert(j, number_of_bits)

                minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

                S = ['0' for m in range(len(X) * 2 - 1)]

                Y.append('0')

                interval_left = len(Y) - 2
                interval_right = len(Y)

                algo.bit_depth = len(S)

                for m in range(len(Y) - 2):
                    two_bits = Y[interval_left:interval_right]

                    if two_bits == ['1', '0']:
                        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
                    elif two_bits == ['0', '1']:
                        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
                    else:
                        S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)

                    interval_left -= 1
                    interval_right -= 1

                Y.pop()

                if S[0] == '1':
                    S = algo.dop(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j, algo.convert(S))
                    self.assertEqual(i * j, algo.convert(S))
