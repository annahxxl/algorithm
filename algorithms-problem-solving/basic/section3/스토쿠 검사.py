sudoku = [list(map(int, input().split())) for _ in range(9)]

def check(sudoku):
  # 행, 열 체크
  for i in range(9):
    row = [0] * 10 # 행 체크 리스트 -> 가로 줄
    col = [0] * 10 # 열 체크 리스트 -> 세로 줄
    for j in range(9):
      row[sudoku[i][j]] = 1
      col[sudoku[j][i]] = 1
    if (sum(row) != 9) or (sum(col) != 9):
      return False
  # 그룹 체크
  for i in range(3):
    for j in range(3):
      group = [0] * 10 # 그룹 체크 리스트
      for k in range(3):
        for t in range(3):
          group[sudoku[i*3+k][j*3+t]] = 1
      if sum(group) != 9:
        return False
  return True

if check(sudoku):
  print('YES')
else:
  print('NO')