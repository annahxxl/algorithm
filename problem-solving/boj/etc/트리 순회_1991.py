class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def pre_order(node): # 전위 순회 (루트 -> 왼쪽 자식 -> 오른쪽 자식)
  print(node.data, end='')
  if node.left != '.':
    pre_order(tree[node.left])
  if node.right != '.':
    pre_order(tree[node.right])

def in_order(node): # 중위 순회 (왼쪽 자식 -> 루트 -> 오른쪽 자식)
  if node.left != '.':
    in_order(tree[node.left])
  print(node.data, end='')
  if node.right != '.':
    in_order(tree[node.right])

def post_order(node): # 후위 순회 (왼쪽 자식 -> 오른쪽 자식 -> 루트)
  if node.left != '.':
    post_order(tree[node.left])
  if node.right != '.':
    post_order(tree[node.right])
  print(node.data, end='')

n = int(input())
tree = dict()
for _ in range(n):
  data, left, right = input().split()
  tree[data] = Node(data, left, right)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])