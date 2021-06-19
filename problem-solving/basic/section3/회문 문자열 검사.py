n = int(input())

for i in range(n):
  str = input()
  str = str.upper()
  for j in range(len(str) // 2):
    if str[j] != str[len(str)-j-1]:
      print("#%d NO" %(i+1))
      break
  else:
    print("#%d YES" %(i+1))