import re
txt = '31.12.2025'
res = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', txt)
print(res[1])
print(res[2])
print(res[3])