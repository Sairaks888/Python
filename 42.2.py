import re
txt = 'ааа ббб ёёё ззз ййй ААА БББ ЁЁЁ ЗЗЗ ЙЙЙ'
txt1= re.findall(r'[а-яА-ЯёЁ]+', txt)
print(txt1)