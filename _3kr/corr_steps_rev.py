import algorithms as algo

x = 9
y = -15

X = algo.convert(x, algo.bit_depth / 2 + 1)
Y = algo.convert(y, algo.bit_depth / 2 + 1)

revX = algo.rev(x, algo.bit_depth / 2 + 1)
revY = algo.rev(y, algo.bit_depth / 2 + 1)
minX = algo.Fullreverse(X.copy())

S = ['0' for i in range(len(X) * 2 - 1)]

print("X = ", X)
print("Y = ", Y)
print("Xrev = ", revX)
print("Yrev = ", revY)
print("-[X]d = ", minX)

corr_flag = False if revY[0] == '0' else True

for i in range(len(Y)):
    anal_bit = revY[i]
    if anal_bit == '1' and i != 0:
        S = algo.addition(S, revX.copy(), len(X) * 2 - 1, code='rev', kr=3)

    if i != len(Y) - 1:
        revX.insert(1, X[0])
        if corr_flag:
            minX.append(minX[0])

if corr_flag:
    S = algo.addition(S, minX, len(X) * 2 - 1, code='rev', kr=3)
    S = algo.addition(S, revX, len(X) * 2 - 1, code='rev', kr=3)

if S[0] == '1':
    S = algo.rev(algo.convert(S, len(S)), len(S))
    print(S)

print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
      str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))
