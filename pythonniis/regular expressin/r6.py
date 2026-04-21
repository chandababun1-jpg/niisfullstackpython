import re 
txt ="The ra16823in sp4a9587i6n" 
x=re.findall("[0-9]+",txt)
print(x)