import re
txt = '2025-12-31 12:59:59'
res = re.split(r'[-: ]', txt)
print(res)