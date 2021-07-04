num_list = []

for _ in range(9):
  num = num_list.append(int(input()))
  
largest = max(num_list)
print(largest)

for i in range(len(num_list)):
  if num_list[i] == largest:
    print(i+1)