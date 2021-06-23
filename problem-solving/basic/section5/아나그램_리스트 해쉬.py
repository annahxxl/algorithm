first = input()
second = input()
s1 = [0] * 52 # 알파벳(대문자+소문자) 개수 : 52
s2 = [0] * 52

# 문자 개수 세기
for x in first:
  if x.isupper():
    s1[ord(x)-65] += 1 # 대문자(ASCII 65 ~ 90) index => 0 ~ 25
  else:
    s1[ord(x)-71] += 1 # 소문자(ASCII 97 ~ 122) index => 26 ~ 51
for x in second:
  if x.isupper():
    s2[ord(x)-65] += 1
  else:
    s2[ord(x)-71] += 1

for i in range(52):
  if s1[i] != s2[i]:
    print('NO')
    break
else:
  print('YES')