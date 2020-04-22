def leapYear(y1, y2):
    num = (y2-y1)//4 + 1
    # print(num)
    for i in range(y1, y2+1, 4):
        if i % 100 == 0 and i % 400 != 0:
            num -= 1
    return num

print(leapYear(772, 1849))