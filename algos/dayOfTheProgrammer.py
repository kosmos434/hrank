# 📆📆


year = 1918


def dayOfProgrammer(year):
    day = 0
    if (year < 1918):
        day = febMath(28)
        if (year % 4) == 0:
            # print('leap year here')
            day = febMath(29)

    if year == 1918:
        day = febMath(15)

    if (year > 1918):
        day = febMath(28)
        if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
            # print('leap year here')
            day = febMath(29)

    return(f'{day}.{9:02d}.{year}')


def febMath(feb):
    return 256 - (31 + feb + 31 + 30 + 31 + 30 + 31 + 31)


dayOfProgrammer(year)
