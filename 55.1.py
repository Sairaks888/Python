import re

txt = 'username:john'
res = re.search(r'(username:)(john)', txt)
print(res.group(1)) 
print(res.group(2)) 