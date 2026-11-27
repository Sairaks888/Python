import re
txt = 'abc 123 def 456 789'
res = re.findall(r'[a-zA-Z]+', txt)
print(res)