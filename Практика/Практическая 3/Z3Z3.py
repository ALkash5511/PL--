"""
n = int(input("Введите сколько прошло минут с начала новых суток: "))

"""

n = int(input("Введите сколько прошло минут с начала новых суток: "))
a = n%1440//60
b = n%1440%60
if a < 10:
    a = "0" + str(a)
if b < 10:
    b = "0" + str(b)
print("Сейчас времени:",a,":",b)