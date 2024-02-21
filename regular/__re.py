import re

result = dir(re)
# re module regular expression

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# result = re.findall("Python",str)
# result = len(result)

#
# result = re.split(" ",str)

# result = re.sub("\s", "-",str)
# result = re.search
result = re.search("Python",str)
# result= result.span()
# result= result.start()
# result= result.end()
# result= result.group()
# result= result.string
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-z]",str)
result = re.findall("[1-5]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)
result = re.findall("..",str)
result = re.findall("[py..on]",str)
result = re.findall("^P",str)
result = re.findall("saat$",str)
result = re.findall("sa*t",str)
result = re.findall("sa+t",str)
result = re.findall("sa?t",str)
result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)
result = re.findall("\APython",str)
result = re.findall("saat\Z",str)
print(result)