import re
txt = 'ab cd ef'
res = re.sub(r'([a-z])([a-z])', r'\2\1', txt)
print(res)