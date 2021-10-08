ml, mr, tl, tr = ('SPR'.index(i) for i in input().split())

# S = 0, P = 1, R = 2

if ml == mr and (ml + 2) % 3 in [tl, tr]:
  print('TK')
elif tl == tr and (tl + 2) % 3 in [ml, mr]:
  print('MS')
else:
  print('?')