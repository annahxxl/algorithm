def check(sudoku):
  for i in range(9):
    row = col = [0] * 10
    for j in range(9):
      row[sudoku[i][j]] = 1
      col[sudoku[j][i]] = 1
    if sum(row) != 9 or sum(col) != 9:
      return False
  for i in range(3):
    for j in range(3):
      group = [0] * 10
      for k in range(3):
        for t in range(3):
          group[sudoku[i*3+k][j*3+t]] = 1
      if sum(group) != 9:
        return False
  return True

sudoku = [list(map(int, input().split())) for _ in range(9)]
if check(sudoku):
  print('YES')
else:
  print('NO')