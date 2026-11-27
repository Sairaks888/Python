import re
txt = '31.12.2025'
res = re.sub(r'(\d{2})\.(\d{2})\.(\d{4})', r'\3.\2.\1', txt)
print(res)