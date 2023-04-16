import sys
import unittest

sys.path.append("../_3kr")
from _3kr import algorithms as algo


class section_multiply(unittest.TestCase):

    def test_section_multiply_AminB(self):
        for i in range(16):
            for j in range(-15, 1):
                x = i
                y = j

                X = algo.convert(x, algo.bit_depth / 2 + 1)
                Y = algo.convert(y, algo.bit_depth / 2 + 1)
                minX = algo.Fullreverse(X.copy())

                S = ['0' for m in range(len(X) * 2 - 1)]

                while len(minX) != len(S):
                    minX.append(minX[0])

                for m in range(1, len(Y)):
                    anal_bit = Y[m]
                    minX = algo.shift(minX, "rev", -1)
                    if anal_bit == '1':
                        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='rev', kr=3)

                if S[0] == '1':
                    S = algo.rev(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j, algo.convert(S.copy()))
                    self.assertEqual(i * j, algo.convert(S))
