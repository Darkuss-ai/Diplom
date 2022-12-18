# -*- coding: windows-1251 -*-

def reverse(A):
    for i in range(len(A) - 1, 0, -1):
        if A[i] == '1':
            A[i] = '0'
        else:
            A[i] = '1'
    return A


def test(A, B, code='str'):
    while len(A) != bit_depth:
        A.insert(0, "0")
    while len(B) != bit_depth:
        B.insert(0, "0")

    C = ["0" for i in range(len(A))]

    if A[0] == '1' and code == 'str':
        A = reverse(A)

    if B[0] == '1' and code == 'str':
        B = reverse(B)

    # print(A)
    # print(B)

    # print(B)

    flag = False
    for i in range(len(A) - 1, -1, -1):
        if i == 0 and ((flag == True) and ((A[i] == '1' and B[i] == '0') or
                                           (A[i] == '0' and B[i] == '1'))
                       or (A[i] == '1' and B[i] == '1')):
            C = test(C, ['1'])

        if (A[i] == '1' and B[i] == '0') or (A[i] == '0' and B[i] == '1'):
            if not flag:
                C[i] = '1'
            else:
                C[i] = '0'
        elif (A[i] == '0' and B[i] == '0'):
            if not flag:
                C[i] = '0'
            else:
                C[i] = '1'
                flag = False
        else:
            if not flag:
                C[i] = '0'
                flag = True
            else:
                C[i] = '1'

    # print(C)
    if code == 'dop':
        C = reverse(C)
    return C


def shift(A, A_rev, A_dop, shft):
    flag = True if A[0] == '1' else False

    print(A, A_rev, A_dop)

    if shft < 0:
        for i in range(-shft):
            A[2:] = A[1:-1]
            A[1] = '0'
        if flag:
            for i in range(-shft):
                A_rev[2:] = A_rev[1:-1]
                A_rev[1] = "1"
            for i in range(-shft):
                A_dop[2:] = A_dop[1:-1]
                A_dop[1] = "1"
        else:
            for i in range(-shft):
                A_rev[2:] = A_rev[1:-1]
                A_rev[1] = "0"
            for i in range(-shft):
                A_dop[2:] = A_dop[1:-1]
                A_dop[1] = "0"
    else:
        for i in range(shft):
            if A[1] == '1':
                A = "ПЕРЕПОЛНЕНИЕ"
                break
            A[1:-1] = A[2:]
            A[-1] = '0'
        if flag:
            for i in range(shft):
                if A_rev[1] == '0':
                    A_rev = "ПЕРЕПОЛНЕНИЕ"
                    break
                A_rev[1:-1] = A_rev[2:]
                A_rev[-1] = "1"
            for i in range(shft):
                if A_dop[1] == '0':
                    A_dop = "ПЕРЕПОЛНЕНИЕ"
                    break
                A_dop[1:-1] = A_dop[2:]
                A_dop[-1] = "1"
        else:
            for i in range(shft):
                if A_rev[1] == '1':
                    A_rev = "ПЕРЕПОЛНЕНИЕ"
                    break
                A_rev[1:-1] = A_rev[2:]
                A_rev[-1] = "0"
            for i in range(shft):
                if A_dop[1] == '1':
                    A_dop = "ПЕРЕПОЛНЕНИЕ"
                    break
                A_dop[1:-1] = A_dop[2:]
                A_dop[-1] = "0"

    print(A, A_rev, A_dop)

    return A, A_rev, A_dop


A = 1
B = 3
A_is_minus = False
B_is_minus = False
if A < 0:
    A_is_minus = True
if B < 0:
    B_is_minus = True

A = bin(A)
B = bin(B)

if not A_is_minus:
    A = list(A[2:])
else:
    A = list(A[3:])
    A[0] = '1'

if not B_is_minus:
    B = list(B[2:])
else:
    B = list(B[3:])

bit_depth = 8

while len(A) != bit_depth:
    A.insert(0, "0")
while len(B) != bit_depth:
    B.insert(0, "0")

if A_is_minus:
    A[0] = '1'
if B_is_minus:
    B[0] = '1'

A_straight = A.copy()
B_straight = B.copy()

print(A_straight, "А в прямом коде")
print(B_straight, "В в прямом коде")

A_rev = A.copy()
B_rev = B.copy()

if A_is_minus:
    for i in range(len(A_rev) - 1, 0, -1):
        if A_rev[i] == '1':
            A_rev[i] = '0'
        else:
            A_rev[i] = '1'

if B_is_minus:
    for i in range(len(B_rev) - 1, 0, -1):
        if B_rev[i] == '1':
            B_rev[i] = '0'
        else:
            B_rev[i] = '1'

print("\n")
print(A_rev, 'A v obratnom kode')
print(B_rev, 'B v obratnom kode')

A_dop = test(A_rev.copy(), ['1']) if A_is_minus else A_rev.copy()
B_dop = test(B_rev.copy(), ['1'], 'dop') if B_is_minus else B_rev.copy()

print(B_dop, "FFFEFEFEFEFEFEFEFEE")

print("\n")

print(A_dop, "A v dopolnitelnom kode")
print(B_dop, "B v dopolnitelnom kode")

minus_A = A.copy()
minus_B = B.copy()

minus_A[0] = '1' if minus_A[0] == '0' else '0'
minus_B[0] = '1' if minus_B[0] == '0' else '0'

print("\n\n\n")

print(minus_A, "-A")
print(minus_B, "-B")

# for i in range(len(A)-1, -1, -1):
#     if A[i] == '1':
#         minus_A.append('0')
#     else:
#         minus_A.append('1')
# minus_A.reverse()


# for i in range(len(B)-1, -1, -1):
#     if B[i] == '1':
#         minus_B.append('0')
#     else:
#         minus_B.append('1')
# minus_B.reverse()

A_is_minus = True if minus_A[0] == '1' else False
B_is_minus = True if minus_B[0] == '1' else False

minus_A_rev = minus_A.copy()
minus_B_rev = minus_B.copy()

if A_is_minus:
    for i in range(len(minus_A_rev) - 1, 0, -1):
        if minus_A_rev[i] == '1':
            minus_A_rev[i] = '0'
        else:
            minus_A_rev[i] = '1'

if B_is_minus:
    for i in range(len(minus_B_rev) - 1, 0, -1):
        if minus_B_rev[i] == '1':
            minus_B_rev[i] = '0'
        else:
            minus_B_rev[i] = '1'

print("\n")

print(minus_A_rev, "-A v obratnom kode")
print(minus_B_rev, "-B v obratnom kode")

minus_A_dop = test(minus_A_rev.copy(), ['1']) if A_is_minus else minus_A_rev.copy()
minus_B_dop = test(minus_B_rev.copy(), ['1'], 'dop') if B_is_minus else minus_B_rev.copy()

print("\n")

print(minus_A_dop, "-A v dopolnitelnom kode")
print(minus_B_dop, "-B v dopolnitelnom kode")

print("\n\n\n")

# A_shift, A_shift_rev, A_shift_dop = shift(A.copy(), A_rev.copy(), A_dop.copy(), -2)
# A_shift1, A_shift_rev1, A_shift_dop1 = shift(A.copy(), A_rev.copy(), A_dop.copy(), -3)

print("\n\n\n\n")

# A_shift2, A_shift_rev2, A_shift_dop2 = shift(A.copy(), A_rev.copy(), A_dop.copy(), 3)
# A_shift3, A_shift_rev3, A_shift_dop3 = shift(A.copy(), A_rev.copy(), A_dop.copy(), 4)


print("\n\n\n\n")

# B_shift, B_shift_rev, B_shift_dop = shift(B.copy(), B_rev.copy(), B_dop.copy(), -2)
# B_shift1, B_shift_rev1, B_shift_dop1 = shift(B.copy(), B_rev.copy(), B_dop.copy(), -3)


print("\n\n\n\n")

# B_shift2, B_shift_rev2, B_shift_dop2 = shift(B.copy(), B_rev.copy(), B_dop.copy(), 3)
# B_shift3, B_shift_rev3, B_shift_dop3 = shift(B.copy(), B_rev.copy(), B_dop.copy(), 4)


print(test(A.copy(), B.copy(), 'str'))
print(test(A_rev.copy(), B_rev.copy(), 'rev'))
a = test(A_dop.copy(), B_dop.copy(), 'str')
print(a)
print(test(minus_A.copy(), minus_B.copy(), 'str'))

tt1 = int('-0b' + ''.join(minus_A), base=2)
tt2 = int('0b' + ''.join(minus_B), base=2)

tt3 = test(minus_A.copy(), minus_B.copy())
print(tt3)

tt3 = int('-0b' + ''.join(tt3), base=2)
