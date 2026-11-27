import re
txt = '123 aaa 456 bbb 789'
res = re.findall(r'\d+', txt)
print(res)