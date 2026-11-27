import re
txt = 'xaz x.z x3z x@z x$z xrz'
txt1 = re.findall(r'x[^.$@]z', txt)
print(txt1)