class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class NodeMgmt:
  def __init__(self, data):
    self.head = Node(data)
    
  def add(self, data):
    if self.head == '':
      self.haed = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
      
  def delete(self, data):
    if self.head == '':
      print("해당 값을 가진 노드가 없습니다.")
      return
    # case 1. head 삭제
    if self.head.data == data:
      tmp = self.head
      self.head = self.head.next
      del tmp
    else:
      node = self.head
      while node.next:
        # case 2. 마지막 노드 삭제 + case 3. 중간 노드 삭제
        if node.next.data == data:
          tmp = node.next
          node.next = node.next.next
          del tmp
          return
        else:
          node = node.next

  def desc(self): # 데이터를 순회하여 출력
    node = self.head
    while node:
      print(node.data)
      node = node.next
      
  # 노드 데이터가 특정 숫자인 노드 찾기
  def search_node(self, data):
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next

linkedlist1 = NodeMgmt(0)
# linkedlist1.desc()

for data in range(1, 10):
  linkedlist1.add(data)

linkedlist1.desc()

print('---------- delete ----------')
linkedlist1.delete(0)
linkedlist1.delete(4)
linkedlist1.delete(9)
linkedlist1.desc()

print('---------- search ----------')
print(linkedlist1.search_node(3))
