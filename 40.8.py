import re
txt = 'aAXa aeffa aGha aza ax23a a3sSa'
print(re.findall(r'a[a-z\d]a', txt))