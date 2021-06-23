first = input()
second = input()
# s1 = dict()
# s2 = dict()

# # 문자 개수 세기
# for x in first:
#   s1[x] = s1.get(x, 0) + 1
# for x in second:
#   s2[x] = s2.get(x, 0) + 1
  
# for key in s1.keys():
#   if key in s2.keys():
#     if s1[key] != s2[key]:
#       print('NO')
#       break
#   else:
#     print('NO')
#     break
# else:
#   print('YES')

# sol2 (개선 코드)
s = dict()

for x in first:
  s[x] = s.get(x, 0) + 1
for x in second:
  s[x] = s.get(x, 0) - 1
  
for x in first:
  # if s[x] > 0:
  if s.get(x) > 0:
    print('NO')
    break
else:
  print('YES')