# First-In, First-Out

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
  queue_list.append(data)

def dequeue():
  data = queue_list[0]
  del queue_list[0]
  return data

for num in range(1, 10):
  enqueue(num)

print(queue_list)

print(dequeue())
print(dequeue())