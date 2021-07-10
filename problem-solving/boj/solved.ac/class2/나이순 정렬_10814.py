n = int(input())
members = []
for _ in range(n):
  age, name = input().split(' ')
  age = int(age)
  members.append((age, name))
  
members.sort(key=lambda x: x[0])
# 참고) 튜플의 첫 번째 원소로 정렬, 이후 같은 값이 나오면 두 번째 원소 정렬하는 방식
# tuple_list.sort(key=lambda x: (x[0], x[1]))
  
for age, name in members:
  print(age, name)