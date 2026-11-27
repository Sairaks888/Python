import re
txt = 'x1z x2z x5z x8z xaz'
print(re.findall(r'x[^2-7]z', txt))