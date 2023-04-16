# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)

dig = (input('Число через знак "." если с разрядами: '))
summ = 0
if dig.isdigit():
    dig = int(dig)
    while dig > 0:
        dig1 = dig % 10
        summ = summ + dig1
        dig = dig // 10
    print(int(summ))

else:
    dig_conv = dig.replace('.', '')
    dig_conv = abs(int(dig_conv))
    while dig_conv > 0:
        dig1 = dig_conv % 10
        summ = summ + dig1
        dig_conv = dig_conv // 10
    print(summ)

