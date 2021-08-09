n = input()
result = list()
for i in n:
  result.append(int(i))
result.sort(reverse=True)
for i in result:
  print(i, end='')

'''
# 9부터 0까지 자릿수 확인
array = input()
for i in range(9, -1, -1):
  for j in array:
    if int(j) == i:
      print(i, end='')
'''