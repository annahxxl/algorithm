word = input()
res = list()

# 문자 -> 아스키코드 : ord(),
# 아스키코드 -> 문자 : chr()
# A :  65, Z : 90
for i in word:
  i = ord(i) - 3
  if i < ord('A'):
    i += 26 # 알파벳 개수
  res.append(chr(i))

res = ''.join(res)
print(res)