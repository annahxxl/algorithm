n = int(input())
nums = list(map(int, input().split()))

lp = 0
rp = n-1
last = 0 # 현재 만들어진 수열의 마지막 항
tmp = []
res = ""

while lp <= rp:
  if nums[lp] > last:
    tmp.append((nums[lp], 'L'))
  if nums[rp] > last:
    tmp.append((nums[rp], 'R'))
  if len(tmp) == 0:
    break
  else:
    tmp.sort()
    res = res + tmp[0][1] # tmp의 첫 번째 tuple의 index가 1인 값
    last = tmp[0][0]
    if tmp[0][1] == 'L':
      lp += 1
    else:
      rp -= 1
  tmp.clear()
  
print(len(res))
print(res)