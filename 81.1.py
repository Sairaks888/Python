class NegativeNumberError(Exception):
    pass
num = -3
try:
    if num > 0:
        print(num ** 2)
    else:
        raise NegativeNumberError
except NegativeNumberError:
    print("Ошибка")