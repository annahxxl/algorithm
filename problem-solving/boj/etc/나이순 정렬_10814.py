n = int(input())
members = list()
for _ in range(n):
  age, name = input().split()
  members.append((int(age), name))
members.sort(key=lambda x: x[0]) # 나이만 정렬할수 있도록 키 값 설정
for age, name in members:
  print(age, name)