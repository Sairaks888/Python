txt = '2'
try:
    res1 = txt + 3
    res2 = txt1
except TypeError:
    print("Ошибка(TypeError)")
except NameError:
    print("Ошибка(NameError)")