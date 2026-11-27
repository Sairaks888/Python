lst = [1, 2, 3, 4]
def getElem(iter):
    try:
        print(iter[4])
    except IndexError:
        print("Ошибка")
getElem(lst)