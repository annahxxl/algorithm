n = int(input())
poem = dict()

for i in range(n):
  word = input()
  poem[word] = 0
  
for i in range(n-1):
  word = input()
  poem[word] = 1 # 시에 쓰인 단어 체크
  
for key, val in poem.items():
  if val == 0:
    print(key)
    break