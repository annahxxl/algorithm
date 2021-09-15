'''
# my solution (dictionary 이용한 풀이)
first = input()
second = input()
f_dic = dict()
s_dic = dict()
for f in first:
  if f not in f_dic:
    f_dic[f] = 1
  else:
    f_dic[f] += 1
for s in second:
  if s not in s_dic:
    s_dic[s] = 1
  else:
    s_dic[s] += 1
if f_dic == s_dic:
  print('YES')
else:
  print('NO')
'''

'''
# other solution (dictionary 이용한 풀이 2)
first = input()
second = input()
str1 = dict()
str2 = dict()
for s in first:
  str1[s] = str1.get(s, 0) + 1 # str1[s]의 value 리턴, 없다면 0 리턴
for s in second:
  str2[s] = str2.get(s, 0) + 1
for i in str1.keys():
  if i in str2.keys():
    if str1[i] != str2[i]:
      print('NO')
      break
  else:
    print('NO')
    break
else:
  print('YES')
'''

'''
# other solution (dictionary 이용한 풀이 3)
first = input()
second = input()
dic = dict()
for s in first:
  dic[s] = dic.get(s, 0) + 1
for s in second:
  dic[s] = dic.get(s, 0) - 1
for s in first:
  if dic.get(s) != 0:
    print('NO')
    break
else:
  print('YES')
'''

# other solution (list 이용한 풀이 - ASCII)
first = input()
second = input()
str1 = [0] * 52
str2 = [0] * 52
for s in first:
  if s.isupper(): # 대문자일 경우 리스트의 index 0 ~ 25 에 저장
    str1[ord(s)-65] += 1
  else: # 소문자일 경우 리스트의 index 26 ~ 51 에 저장
    str1[ord(s)-71] += 1
for s in second:
  if s.isupper():
    str2[ord(s)-65] += 1
  else:
    str2[ord(s)-71] += 1
for i in range(51):
  if str1[i] != str2[i]:
    print('NO')
    break
else:
  print('YES')