'''
price = int(input())
en = [500, 100, 50, 10, 5, 1]
cnt = 0
change = 1000 - price
for i in range(len(en)):
  tmp = change // en[i]
  cnt += tmp
  change -= (tmp * en[i])
print(cnt)
'''

change = 1000 - int(input())
cnt = 0
for i in [500, 100, 50, 10, 5, 1]:
  cnt += change // i
  change %= i
print(cnt)