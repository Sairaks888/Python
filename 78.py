lst = [1, 2, 3]
try:
    res = 1 / 1
except ZeroDivisionError:
    print("Ошибка")
else:
    print(len(lst)) 