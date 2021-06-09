t = int(input())

for _ in range(t):
  n = int(input())
  bin_list = bin(n)[2:] # 2진수 형태는 앞에 ob가 붙으므로
  for idx, val in enumerate(bin_list[::-1]):
    if val == '1':
      print(idx, end=' ')