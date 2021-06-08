# Last-In, First-Out

# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기
stack_list = list()

stack_list.append(1)
stack_list.append(2)

print(stack_list.pop())

# 리스트 변수로 스택을 다루는 push, pop 기능 구현해보기
# push, pop 함수 사용하지 않고 직접 구현해보기
stack_list = list()

def push(data):
  stack_list.append(data)
  
def pop():
  data = stack_list[-1]
  del stack_list[-1]
  return data

for num in range(1, 10):
  push(num)
  
print(stack_list)

print(pop())
print(pop())
