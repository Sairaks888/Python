import re
txt = 'aaa bbb 123 456'
res = re.search(r'(?P<first>[a-zA-Z]+)\s(?P<second>[a-zA-Z]+)', txt)
print(res.groupdict())