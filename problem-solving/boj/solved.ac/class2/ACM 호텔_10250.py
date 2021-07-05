T = int(input())

# for _ in range(T):
#   H, W, N = map(int, input().split(' '))
#   cnt = 0
#   for i in range(W):
#     for j in range(H):
#       cnt += 1
#       if cnt == N:
#         f = str(j+1)
#         ho = str(i+1)
#         print(f, ho.zfill(2), sep='')
#         break
      
# 다른 사람의 풀이
# N에서 건물 층수를 나눈 나머지가 객실의 층수
# N에서 건물 층수를 나눈 (몫 + 1)이 객실의 호수
for _ in range(T):
    H, W, N = map(int, input().split(' '))
    floor = N % H
    num = N // H + 1
    if N % H == 0:
      floor = H
      num = N // H
    print(floor*100+num)