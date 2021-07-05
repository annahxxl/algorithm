# 노드 클래스 만들기
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
# 이진 탐색 트리에 데이터 넣기
class NodeMgmt:
  def __init__(self, head):
    self.head = head
    
  def insert(self, value):
    self.current_node = self.head # 비교할 노드
    while True:
      if value < self.current_node.value:
        if self.current_node.left != None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value)
          break
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break
        
  def search(self, value):
    self.current_node = self.head
    while self.current_node:
      if self.current_node.value == value:
        return True
      elif value < self.current_node.value:
        self.current_node = self.current_node.left
      else:
        self.current_node = self.current_node.right
    return False
  
  def delete(self, value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
      if self.current_node.value == value:
        searched = True
        break
      elif value < self.current_node.value:
        self.parent = self.current_node
        self.current_node = self.current_node.left
      else:
        self.parent = self.current_node
        self.current_node = self.current_node.right
    if searched == False:
      return False
    # 여기부터 case들을 분리해 코드 작성
    # -> self.current_node가 삭제할 Node, self.parent가 삭제할 Node의 부모 Node인 상태
    # case1: 삭제할 Node가 Leaf Node인 경우 (자식 Node ❌)
    if self.current_node.left == None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = None
      else:
        self.parent.right = None
      del self.current_node
    # case2-1: 삭제할 Node가 자식 Node를 왼쪽에 한 개 가지고 있을 경우
    if self.current_node.left != None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = self.current_node.left
      else:
        self.parent.right = self.current_node.right
    # case2-2: 삭제할 Node가 자식 Node를 오른쪽에 한 개 가지고 있을 경우
    if self.current_node.left == None and self.current_node.right != None:
      if value < self.parent.value:
        self.parent.left = self.current_node.right
      else:
        self.parent.right = self.current_node.right
    
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(7))