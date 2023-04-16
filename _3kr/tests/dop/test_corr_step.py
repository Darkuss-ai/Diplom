import sys
import unittest

sys.path.append("../_3kr")
from _3kr import algorithms as algo


class corr_step(unittest.TestCase):

    def test_corr_step_minAB(self):
        for i in range(-15, 16):
            for j in range(16):

                x = i
                y = j

                X = algo.convert(x, algo.bit_depth / 2 + 1)
                Y = algo.convert(y, algo.bit_depth / 2 + 1)

                dopX = algo.dop(x, algo.bit_depth / 2 + 1)
                dopY = algo.dop(y, algo.bit_depth / 2 + 1)

                minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

                S = ['0' for n in range(len(X) * 2 - 1)]

                for m in range(len(Y)):
                    anal_bit = dopY[m]
                    if anal_bit == '1' and m == 0:
                        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    elif anal_bit == '1':
                        S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    dopX.insert(1, X[0])

                if S[0] == '1':
                    S = algo.dop(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j)
                    self.assertEqual(i * j, algo.convert(S))

    def test_corr_step_AminB(self):
        for i in range(16):
            for j in range(-15, 16):

                x = i
                y = j

                X = algo.convert(x, algo.bit_depth / 2 + 1)
                Y = algo.convert(y, algo.bit_depth / 2 + 1)

                dopX = algo.dop(x, algo.bit_depth / 2 + 1)
                dopY = algo.dop(y, algo.bit_depth / 2 + 1)

                minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

                S = ['0' for n in range(len(X) * 2 - 1)]

                for m in range(len(Y)):
                    anal_bit = dopY[m]
                    if anal_bit == '1' and m == 0:
                        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    elif anal_bit == '1':
                        S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
                    dopX.insert(1, X[0])

                if S[0] == '1':
                    S = algo.dop(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j, algo.convert(S.copy()))
                    self.assertEqual(i * j, algo.convert(S))
