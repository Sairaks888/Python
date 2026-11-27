class ZeroError(Exception):
    pass

num = 0

try:
    if num == 0:
        raise ZeroError("")
    print(f"{num}")
except ZeroError as e:
    print(f"Ошибка{e}")