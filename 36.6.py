import re
txt = '[abc] {abc} abc (abc) [abc]'
txt1 = re.sub(r'\[abc\]', '!', txt)
print(txt1)
