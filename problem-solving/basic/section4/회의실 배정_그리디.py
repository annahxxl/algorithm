n = int(input())
meeting = []

for _ in range(n):
  s, e = map(int, input().split())
  meeting.append((s, e))
  
# 정렬 기준을 e로 바꾸고 정렬하기
meeting.sort(key = lambda x : (x[1], x[0]))

et = 0 # end time
cnt = 0

for s, e in meeting:
  if s >= et:
    cnt += 1
    et = e
    
print(cnt)