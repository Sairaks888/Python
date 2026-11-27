txt = 'abc'
try:
    res = txt + 2
except TypeError:
    print("Ошибка")
finally:
    print(txt.upper())