def convert_temp(value, unit="C"):
     if unit == "C":
        c = (value - 32) * (5 / 9)
        print(c, '°C')
        #return c
     elif unit == "F":
        f = (value * 1.8) + 32
        print(f, '°F')
        #return f
print(convert_temp(value = int(input("Введите значение: ")), unit = input("Введите:\n C - Цельсий\n F - Фаренгейт\n")))