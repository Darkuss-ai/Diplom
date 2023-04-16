import sys
import unittest

sys.path.append("../_3kr")
from _3kr import algorithms as algo


class adjacent(unittest.TestCase):

    def test_adjacent(self):
        for i in range(-15, 16):
            for j in range(-15, 16):

                x = i
                y = j

                X = algo.convert(x, algo.bit_depth / 2 + 1)
                Y = algo.convert(y, algo.bit_depth / 2 + 1)

                dopX = algo.dop(x, algo.bit_depth / 2 + 1)
                dopY = algo.dop(y, algo.bit_depth / 2 + 1)

                if len(dopY) % 2 != 0:
                    dopY.append("0")

                S = ['0' for m in range(len(X) * 2 - 1)]

                minXdop = algo.Fullreverse(dopX.copy())
                minXdop = algo.addition(minXdop, ['1'], code='dop', bits=len(minXdop))

                interval_left = 0
                interval_right = 2

                for m in range(len(dopY) - 1):
                    two_bits = dopY[interval_left:interval_right]

                    if two_bits == ['1', '0']:
                        S = algo.addition(S, minXdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    elif two_bits == ["0", "1"]:
                        S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    dopX.insert(1, dopX[0])
                    minXdop.insert(1, minXdop[0])

                    interval_left += 1
                    interval_right += 1

                if S[0] == '1':
                    S = algo.dop(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j, algo.convert(S.copy()))
                    self.assertEqual(i * j, algo.convert(S))
