import re
input_string = "This is an;example,string:with.multiple|delimiters"
delimiters = ";|,|:|\\.|\\|"
split_string = re.split(delimiters, input_string)
print(split_string)


txt = "2+2*2"

from solver import solve

print(solve(txt))