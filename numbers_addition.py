# Addition of single-digit number

a = '9999'
b = '9999'


def single_digit_addition(num1, num2):
    sm, rem = 0, 0
    final = ''
    for idx in range(len(num1)-1, -1, -1):
        sm = rem + int(num1[idx]) + int(num2[idx])
        rem = sm // 10
        final += str(sm % 10)

    if rem:
        final += str(rem)

    return "".join(list(reversed(final)))


print(single_digit_addition(a, b))


