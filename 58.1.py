import re
txt = '12 34 56 78'
res = re.sub(r'(\d)(\d)', r'\2\1', txt)
print(res)