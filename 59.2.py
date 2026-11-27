import re
txt = '2025:12:31'
res = re.sub(r'(\d{4}):(\d{2}):(\d{2})', r'\3-\2-\1', txt)
print(res)