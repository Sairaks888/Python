lst = [10, 20, 30, 40, 50]
try:
    index = int(input("144 "))
    print(f"5 {lst[index]}")
except IndexError:
    print("Ошибка нет элемента")
except ValueError:
    print("Ошибка" \
    "")