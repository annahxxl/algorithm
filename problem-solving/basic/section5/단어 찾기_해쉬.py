'''
# my solution
n = int(input())
note = [input() for _ in range(n)]
for _ in range(n-1):
  note.remove(input())
print(note.pop())
'''

# other solution
n = int(input())
note = dict()
for _ in range(n):
  word = input()
  note[word] = 0
for _ in range(n-1):
  word = input()
  note[word] = 1
for key, val in note.items():
  if val == 0:
    print(key)
    break