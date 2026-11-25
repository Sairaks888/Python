def func2(iter):
    def func1(num):
        if num > 0:
            num += 2
        return num
    res = []
    for el in iter:
        res.append(func1(el))
    return res
print(func2([1, -2, 3, -4]))