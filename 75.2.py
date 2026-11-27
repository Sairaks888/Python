import math
try:
    num = float(input("12 "))
    result = math.sqrt(num)
    print(f"2: {result}")
except ValueError:
    print("Ошибка")