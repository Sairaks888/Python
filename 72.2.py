import re
txt = '<a href="" class="eee" id="zzz">'
res = re.findall(r'\w+(?==)', txt)
print(res)