import re
txt = '2025-12-31'
res = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', txt)
print(res[1]) 
print(res[2]) 
print(res[3]) 