n = int(input())
scores = list(map(int, input().split()))
# avg = round(sum(scores) / n) # 파이썬에서 round는 round_half_even방식을 택함
avg = sum(scores) / n
avg = avg + 0.5
avg = int(avg)
min = 2147000000

for idx, score in enumerate(scores): # 리스트 index와 value를 쌍으로 리턴
  diff = abs(score - avg)
  if diff < min:
    min = diff
    res = score # 점수가 평균에 가까운 학생의 점수 저장
    student = idx + 1 # 점수가 평균에 가까운 학생의 번호 저장
  elif diff == min:
    if score > res:
      res = score
      student = idx + 1
      
print(avg, student)