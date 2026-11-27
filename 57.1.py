import re
txt = '12:59:59'
res = re.search(r'(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)', txt)
print(res.groupdict())