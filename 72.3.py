import re
txt = '$aaa $bbb $ccc xxxx'
res = re.findall(r'(?<=\$)\w+', txt)
print(res)