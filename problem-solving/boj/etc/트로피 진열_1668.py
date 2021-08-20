'''
# my solution
n = int(input())
shelf = list()
for _ in range(n):
  shelf.append(int(input()))
l_max = r_max = l_cnt = r_cnt = 0
r_shelf = list(reversed(shelf))
for i in range(n):
  if shelf[i] > l_max:
    l_max = shelf[i]
    l_cnt += 1
  if r_shelf[i] > r_max:
    r_max = r_shelf[i]
    r_cnt += 1
print(l_cnt)
print(r_cnt)
'''

# other solution
def ascending(array):
  now = array[0]
  result = 1
  for i in range(1, len(array)):
    if now < array[i]:
      result += 1
      now = array[i]
  return result
n = int(input())
array = list()
for _ in range(n):
  array.append(int(input()))
print(ascending(array))
array.reverse()
print(ascending(array))