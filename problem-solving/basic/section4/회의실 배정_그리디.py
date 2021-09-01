n = int(input())
meeting = list()
for _ in range(n):
  s, e = map(int, input().split())
  meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))
cnt = 0
et = 0 # end time
for s, e in meeting:
  if s >= et:
    cnt += 1
    et = e
print(cnt)