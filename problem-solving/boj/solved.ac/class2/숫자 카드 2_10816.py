# 시간 초과
# import sys
# n = int(sys.stdin.readline())
# card_nums = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# check_nums = list(map(int, sys.stdin.readline().split()))

# cnt_list = []
# for a in check_nums:
#   cnt = 0
#   for b in card_nums:
#     if b == a:
#       cnt += 1
#   cnt_list.append(cnt)
  
# for i in cnt_list:
#   print(i, end=' ')    

# 딕셔너리 사용
n = int(input())
card_nums = list(map(int, input().split(' ')))
card_nums.sort()

m = int(input())
check_nums = list(map(int, input().split(' ')))

dic = dict()

for i in card_nums:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in check_nums:
  if i in dic:
    print(dic[i], end=' ')
  else:
    print(0, end=' ')