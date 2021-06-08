# Node 구현
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
head = node1

# 링크드 리스트로 데이터 추가하기
def add(data):
  node = head
  while node.next:
    node = node.next
  node.next = Node(data)

for data in range(2, 10):
  add(data)

# 링크드 리스트 데이터 출력하기 (검색하기)
node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data) # 마지막 노드

# 링크드 리스트 데이터 사이에 데이터를 추가
print('---------- insert ----------')
node3 = Node(1.5)
node = head
search = True
while search:
  if node.data == 1:
    search = False
  else:
    node = node.next

tmp = node.next
node.next = node3
node3.next = tmp

# 링크드 리스트 데이터 출력하기 (검색하기)
node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data) # 마지막 노드