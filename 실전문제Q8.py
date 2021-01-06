# 문자열 재정렬
data = input()
num  = 0
text = []

for i in data:
  if i.isalpha() :
    text.append(i)
  else:
    num += int(i)

text.sort()
if num != 0:
  text.append(str(num))

print(''.join(text))
