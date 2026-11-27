import re

txt = '12345'
res = re.fullmatch(r'\d+', txt)
if res:
    print("Состоит только из цифр")
else:
    print("Состоит не только из цифр")