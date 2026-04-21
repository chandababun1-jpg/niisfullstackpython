import re
result = re.match(r'\d+', '123ab45c')
print(result.group())