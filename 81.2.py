class ZeroError(Exception):
    pass
num = 0
try:
    if num != 0:
        print(num + 5)
    else:
        raise ZeroError
except ZeroError:
    print("Ошибка")