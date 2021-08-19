'''
# my solution
n = int(input())
for i in range(n):
  s = input().upper()
  for j in range(len(s)//2):
    if s[j] != s[-(j+1)]:
      print('#%d NO' %(i+1))
      break
  else:
    print('#%d YES' %(i+1))
'''

# other solution
n = int(input())
for i in range(n):
  s = input().upper()
  if s == s[::-1]:
    print('#%d YES' %(i+1))
  else:
    print('#%d NO' %(i+1))