import sys
import unittest

sys.path.append("../_3kr")
from _3kr import algorithms as algo


class corr_steps(unittest.TestCase):

    def test_corr_steps_AminB(self):
        for i in range(16):
            for j in range(-15, 16):

                x = i
                y = j

                X = algo.convert(x, algo.bit_depth / 2 + 1)
                Y = algo.convert(y, algo.bit_depth / 2 + 1)

                revX = algo.rev(x, algo.bit_depth / 2 + 1)
                revY = algo.rev(y, algo.bit_depth / 2 + 1)
                minX = algo.Fullreverse(X.copy())

                S = ['0' for n in range(len(X) * 2 - 1)]


                corr_flag = False if revY[0] == '0' else True

                for m in range(len(Y)):
                    anal_bit = revY[m]
                    if anal_bit == '1' and m != 0:
                        S = algo.addition(S, revX.copy(), len(X) * 2 - 1, code='rev', kr=3)

                    if m != len(Y) - 1:
                        revX.insert(1, X[0])
                        if corr_flag:
                            minX.append(minX[0])

                if corr_flag:
                    S = algo.addition(S, minX, len(X) * 2 - 1, code='rev', kr=3)
                    S = algo.addition(S, revX, len(X) * 2 - 1, code='rev', kr=3)

                if S[0] == '1':
                    S = algo.rev(algo.convert(S, len(S)), len(S))

                with self.subTest(i=i, j=j):
                    print(i, j, algo.convert(S.copy()))
                    self.assertEqual(i * j, algo.convert(S))
