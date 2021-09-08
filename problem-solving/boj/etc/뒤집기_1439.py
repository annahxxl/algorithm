s = input()
cnt0 = 0
cnt1 = 0
if s[0] == '1': # 모두 0으로 만드는 경우
  cnt0 += 1
else: # 모두 1로 만드는 경우
  cnt1 += 1
for i in range(1, len(s)):
  if s[i] != s[i-1]:
    if s[i] == '1': # 문자열이 0에서 1로 바뀐 경우
      cnt0 += 1
    else: # 문자열이 1에서 0으로 바뀐 경우
      cnt1 += 1
print(min(cnt0, cnt1))