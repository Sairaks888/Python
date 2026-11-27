class NegativeNumberError(Exception):
    pass
num = -6
try:
    if num < 0:
        raise NegativeNumberError
    print(f"{num}")
except NegativeNumberError as e:
    print(f"Ошибка {e}")