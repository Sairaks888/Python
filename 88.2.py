import dateparser
date1 = dateparser.parse('12 января 2025')
date2 = dateparser.parse('вчера')
date3 = dateparser.parse('2024-12-31 15:30')
print("Дата 1:", date1)
print("Дата 2:", date2)
print("Дата 3:", date3)