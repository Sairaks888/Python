import random
def create_generator(start, end):
    last_num = None 
    def get_random():
        nonlocal last_num
        while True:
            num = random.randint(start, end)
            if num != last_num:
                last_num = num  
                return num
    return get_random
rand = create_generator(1, 5)
for _ in range(10):
    print(rand(), end=' ')