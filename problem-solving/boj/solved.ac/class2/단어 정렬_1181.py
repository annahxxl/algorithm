n = int(input())
words = []
for _ in range(n):
  words.append(input())
  
words = list(set(words)) # 중복 제거
words.sort() # 괄호 안 아무 값도 넣지 않으면 사전 순 정렬
words.sort(key=len) # 문자열 길이 순 정렬

for word in words:
  print(word)
  
# 다른 풀이
# N = int(input())
# word = []

# for _ in range(N):
#     word.append(input())

# word = list(set(word))
# word.sort(key=lambda x : (len(x),x))

# print("\n".join(word))