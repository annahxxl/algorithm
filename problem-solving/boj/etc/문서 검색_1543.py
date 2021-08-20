doc = input()
search = input()
index, result = 0, 0
while index < len(doc):
  if doc[index:index+len(search)] == search:
    result += 1
    index += len(search)
  else:
    index += 1
print(result)