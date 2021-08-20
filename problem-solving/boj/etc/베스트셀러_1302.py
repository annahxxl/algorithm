n = int(input())
dic = dict()
for _ in range(n):
  title = input()
  if title not in dic:
    dic[title] = 1
  else:
    dic[title] += 1
MAX = max(dic.values())
result = list()
for title, cnt in dic.items():
  if cnt == MAX:
    result.append(title)
print(sorted(result)[0])