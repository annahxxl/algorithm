# 재귀 함수를 활용하여 1부터 num까지의 곱이 출력되게 만드세요
def multiple(num):
  if num <= 1:
    return num
  return num * multiple(num - 1)
print(multiple(10))

# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
def sum_list(data):
  if len(data) <= 1:
    return data[0]
  return data[0] + sum_list(data[1:])
import random
data = random.sample(range(100), 10)
print(sum_list(data))

# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
def palindrome(string):
  if len(string) <= 1:
    return True
  if string[0] == string[-1]:
    return palindrome(string[1:-1])
  else:
    return False
print(palindrome('MOTOR'))

# 1. 정수 n에 대해
# 2. n이 홀수이면 3 X n + 1 을 하고,
# 3. n이 짝수이면 n 을 2로 나눕니다.
# 4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.
def func(n):
  print(n)
  if n == 1:
    return n
  if n % 2 == 1:
    return func(int((3*n)+1))
  else:
    return func(int(n/2))
func(3)

# 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
# 1 + 3
# 3 + 1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
def func2(data):
  if data == 1:
    return 1
  elif data == 2:
    return 2
  elif data == 3:
    return 4
  return func2(data-1) + func2(data-2) + func2(data-3)
print(func2(5))