import algorithms as algo

x = 4
y = -15

X = algo.convert(x, algo.bit_depth / 2 + 1)
Y = algo.convert(y, algo.bit_depth / 2 + 1)

dopX = algo.dop(x, algo.bit_depth / 2 + 1)
dopY = algo.dop(y, algo.bit_depth / 2 + 1)

if len(dopY) % 2 != 0:
    dopY.append("0")

S = ['0' for i in range(len(X) * 2 - 1)]

minXdop = algo.Fullreverse(dopX.copy())
minXdop = algo.addition(minXdop, ['1'], code='dop', bits=len(minXdop))


print("X = ", X)
print("Y = ", Y)
print("[X]d = ", dopX)
print("[Y]d = ", dopY)
print("-[X]d = ", minXdop)

interval_left = 0
interval_right = 2

for i in range(len(dopY) - 1):
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
    print(S)

print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
      str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))
