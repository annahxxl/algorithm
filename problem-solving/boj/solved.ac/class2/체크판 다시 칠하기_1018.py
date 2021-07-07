n, m = map(int, input().split(' '))
board = []
for _ in range(n):
  board.append(input())

paint_cnt = []

for i in range(n-7):
  for j in range(m-7):
    start_w = 0
    start_b = 0
    for row in range(i, i+8):
      for col in range(j, j+8):
        if (row+col) % 2 == 0:
          if board[row][col] != 'W':
            start_w += 1
          if board[row][col] != 'B':
            start_b += 1
        else:
          if board[row][col] != 'B':
            start_w += 1
          if board[row][col] != 'W':
            start_b += 1
    paint_cnt.append(start_w)
    paint_cnt.append(start_b)
    
print(min(paint_cnt))