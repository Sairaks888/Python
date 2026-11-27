try:
    num1 = float(input("24: "))
    num2 = float(input("66: "))
    result = num1 / num2
    print(f"{result}")
except ZeroDivisionError:
    print('Ошибка')