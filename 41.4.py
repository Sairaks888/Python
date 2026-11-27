import re
txt = 'x6z x@#z xABCz x123z x6!z'
print(re.findall(r'x[^a-zA-Z1-5]+z', txt))