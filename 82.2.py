from my_exceptions import NegativeNumberError, ZeroError
def process_number(num):
    if num < 0:
        raise NegativeNumberError
    if num == 0:
        raise ZeroError
    else:
        return num * 3
try:
    num = -5 
    res = process_number(num)
    print(f"{res}")
except NegativeNumberError:
    print("Ошибка: число  отрицательное")
except ZeroError:
    print("Ошибка: число ноль")